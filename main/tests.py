from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from main.models import Experience, Organization


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.organization = Organization.objects.create(
            name="Himpunan Mahasiswa Fasilkom",
            role="Staff Ahli",
            description="Mengembangkan program kerja keilmuan.",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("main:get_experience_json"))

    def test_experience_json(self):
        data = self.client.get(reverse("main:get_experience_json")).json()
        self.assertEqual(data[0]["fields"]["title"], self.experience.title)
        self.assertEqual(data[0]["fields"]["category_display"], "Part-Time")
        self.assertTrue(data[0]["fields"]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        data = self.client.get(reverse("main:get_experience_json")).json()

        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(data[0]["fields"]["is_ongoing"])

    def test_organization_model(self):
        self.assertEqual(str(self.organization), "Himpunan Mahasiswa Fasilkom")
        self.assertTrue(self.organization.is_ongoing)

    def test_organization_page(self):
        response = self.client.get(reverse("main:show_organization"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "organization.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("main:get_organization_json"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_organization_json(self):
        data = self.client.get(reverse("main:get_organization_json")).json()
        fields = data[0]["fields"]

        self.assertEqual(fields["name"], self.organization.name)
        self.assertEqual(fields["role"], self.organization.role)
        self.assertEqual(fields["description"], self.organization.description)
        self.assertTrue(fields["is_ongoing"])

    def test_empty_organization_page(self):
        Organization.objects.all().delete()
        response = self.client.get(reverse("main:get_organization_json"))

        self.assertEqual(response.json(), [])

    def test_create_experience_ajax_access(self):
        url = reverse("main:create_experience_ajax")
        payload = {"title": "Baru", "description": "Deskripsi", "category": "internship"}

        # GET ditolak (@require_POST)
        self.assertEqual(self.client.get(url).status_code, 405)
        # Pengunjung belum login ditolak
        self.assertEqual(self.client.post(url, payload).status_code, 403)

        # User biasa ditolak
        User.objects.create_user("biasa", password="pw12345!")
        self.client.login(username="biasa", password="pw12345!")
        self.assertEqual(self.client.post(url, payload).status_code, 403)

        # Owner (superuser) diizinkan
        User.objects.create_superuser("owner", "o@x.com", "pw12345!")
        self.client.login(username="owner", password="pw12345!")
        self.assertEqual(self.client.post(url, payload).status_code, 201)
        self.assertTrue(Experience.objects.filter(title="Baru").exists())

        # Input tidak valid ditolak dan tidak tersimpan
        bad = {**payload, "title": '<img src="x" onerror="alert(1)">'}
        self.assertEqual(self.client.post(url, bad).status_code, 400)
        self.assertEqual(Experience.objects.filter(title__icontains="img").count(), 0)

    def test_create_organization_ajax_access(self):
        url = reverse("main:create_organization_ajax")
        payload = {"name": "Org Baru", "role": "Anggota", "status": "Active", "description": "Deskripsi"}

        self.assertEqual(self.client.get(url).status_code, 405)
        self.assertEqual(self.client.post(url, payload).status_code, 403)

        User.objects.create_superuser("owner", "o@x.com", "pw12345!")
        self.client.login(username="owner", password="pw12345!")
        self.assertEqual(self.client.post(url, payload).status_code, 201)
        self.assertTrue(Organization.objects.filter(name="Org Baru").exists())
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select
from main.models import Experience, Organization
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "ended_at",
        ]
        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori",
            "ended_at": "Selesai Pada",
        }
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Contoh: Software Engineer Intern",
                "maxlength": 255,
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ceritakan pengalaman atau tanggung jawabmu...",
                "rows": 4,
            }),
            "category": Select(attrs={
                "class": "form-control",
            }),
            "ended_at": DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local",
            }),
        }

    def clean_title(self):
            title = strip_tags(self.cleaned_data["title"]).strip()
            if not title:
                raise ValidationError("Judul pengalaman tidak boleh hanya berisi tag HTML.")
            return title
    
    def clean_description(self):
            return strip_tags(self.cleaned_data["description"]).strip()

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = [
            "name",
            "role",
            "status",
            "is_active",
            "description",
        ]
        labels = {
            "name": "Nama Organisasi",
            "role": "Peran / Jabatan",
            "status": "Status",
            "is_active": "Masih Aktif?",
            "description": "Deskripsi Organisasi",
        }
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nama Organisasi/Klub",
            }),
            "role": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Contoh: Ketua Departemen",
            }),
            "status": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Contoh: Active Member",
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Deskripsikan kegiatanmu di organisasi ini...",
                "rows": 4,
            }),
        }

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"]).strip()
        if not name:
            raise ValidationError("Nama organisasi tidak boleh hanya berisi tag HTML.")
        return name

    def clean_role(self):
        return strip_tags(self.cleaned_data["role"]).strip()

    def clean_status(self):
        return strip_tags(self.cleaned_data["status"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
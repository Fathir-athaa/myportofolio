# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.models import Experience, Organization
from main.forms import ExperienceForm, OrganizationForm

def show_main(request):
    """Menampilkan halaman utama portofolio."""
    context = {
        'name': 'Portofolio Saya',
    }
    return render(request, 'index.html', context)

def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize("json", json_response.content.decode("utf-8"))
    experience_list = [exp.object for exp in experiences]

    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect('main:show_experience')

    context = {
        'name': 'Portofolio Saya',
        'experience_list': experience_list,
        'form': form,
        'title_query': request.GET.get("title", "").strip(),
    }
    return render(request, 'experience.html', context)


def show_organization(request):
    name_query = request.GET.get("name", "").strip()
    json_response = get_organization_json(request)
    organizations = serializers.deserialize("json", json_response.content.decode("utf-8"))
    organization_list = [org.object for org in organizations]

    form = OrganizationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Organization baru berhasil ditambahkan!")
        return redirect('main:show_organization')

    context = {
        'name': 'Portofolio Saya',
        'organization_list': organization_list,
        'form': form,
        'name_query': name_query,
    }
    return render(request, 'organization.html', context)

def add_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_experience')
    context = {'form': form}
    return render(request, 'experience_form.html', context)

def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diperbarui!")
        return redirect('main:show_experience')
    context = {
        'name': 'Portofolio Saya',
        'form': form,
        'experience': experience,
    }
    return render(request, 'experience_edit_form.html', context)

def add_organization(request):
    form = OrganizationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_organization')
    context = {'form': form}
    return render(request, 'organization_form.html', context)

def edit_organization(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    form = OrganizationForm(request.POST or None, instance=organization)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Organization berhasil diperbarui!")
        return redirect('main:show_organization')
    context = {
        'name': 'Portofolio Saya',
        'form': form,
        'organization': organization,
    }
    return render(request, 'organization_edit_form.html', context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all().order_by('-started_at')

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")


def get_experience_xml(request):
    experiences = Experience.objects.all().order_by('-started_at')
    experience_xml = serializers.serialize("xml", experiences)
    return HttpResponse(experience_xml, content_type="application/xml")


def get_organization_json(request):
    name_query = request.GET.get("name", "").strip()
    organizations = Organization.objects.all()

    if name_query:
        organizations = organizations.filter(name__icontains=name_query)

    organization_json = serializers.serialize("json", organizations)
    return HttpResponse(organization_json, content_type="application/json")


def get_organization_xml(request):
    organizations = Organization.objects.all()
    organization_xml = serializers.serialize("xml", organizations)
    return HttpResponse(organization_xml, content_type="application/xml")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect('main:show_experience')
    return redirect('main:show_experience')


def delete_organization(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    if request.method == "POST":
        organization.delete()
        messages.success(request, "Organization berhasil dihapus!")
        return redirect('main:show_organization')
    return redirect('main:show_organization')
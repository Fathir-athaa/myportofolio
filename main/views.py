# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
import datetime
from main.models import Experience, Organization
from main.forms import ExperienceForm, OrganizationForm

def show_main(request):
    """Menampilkan halaman utama portofolio."""
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        'name': 'Portofolio Saya',
        'last_login': last_login,
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

@login_required(login_url="/login/")
def add_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_experience')
    context = {'form': form}
    return render(request, 'experience_form.html', context)

@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
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

@login_required(login_url="/login/")
def add_organization(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = OrganizationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_organization')
    context = {'form': form}
    return render(request, 'organization_form.html', context)

@login_required(login_url="/login/")
def edit_organization(request, organization_id):
    if not request.user.is_superuser:
        raise PermissionDenied
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

    experience_json = serializers.serialize("json", experiences, use_natural_foreign_keys=True)
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

    organization_json = serializers.serialize("json", organizations, use_natural_foreign_keys=True)
    return HttpResponse(organization_json, content_type="application/json")


def get_organization_xml(request):
    organizations = Organization.objects.all()
    organization_xml = serializers.serialize("xml", organizations)
    return HttpResponse(organization_xml, content_type="application/xml")

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect('main:show_experience')
    return redirect('main:show_experience')

@login_required(login_url="/login/")
def delete_organization(request, organization_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    organization = get_object_or_404(Organization, pk=organization_id)
    if request.method == "POST":
        organization.delete()
        messages.success(request, "Organization berhasil dihapus!")
        return redirect('main:show_organization')
    return redirect('main:show_organization')

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
        return redirect('main:show_experience')
    return redirect('main:show_experience')


@login_required(login_url="/login/")
def toggle_star_organization(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    if request.method == "POST":
        if request.user in organization.starred_by.all():
            organization.starred_by.remove(request.user)
        else:
            organization.starred_by.add(request.user)
        return redirect('main:show_organization')
    return redirect('main:show_organization')

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")
    context = {
        "name": "Portofolio Saya",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    context = {
        "name": "Portofolio Saya",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response
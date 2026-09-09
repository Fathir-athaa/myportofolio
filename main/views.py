from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Fathir Atha Rizki Tasril",
        "npm": "2506656734",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An Information Systems student specializing in systems analysis, software engineering, and data exploration. Possesses a strong technical foundation and a logical mindset to translate complex requirements into structured, efficient, and impactful digital solutions."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Fathir Atha Rizki Tasril",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

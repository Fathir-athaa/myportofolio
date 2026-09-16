from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select
from main.models import Experience, Organization

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
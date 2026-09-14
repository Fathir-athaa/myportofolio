from django.contrib import admin
from main.models import Experience,ExperienceImage,Organization,OrganizationImage

class ExperienceImageInline(admin.TabularInline):
    model = ExperienceImage
    extra = 35

class OrganizationImageInline(admin.TabularInline):
    model = OrganizationImage
    extra = 3

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceImageInline]
    list_display = ('title', 'category', 'is_ongoing')

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [OrganizationImageInline]
    list_display = ('name', 'role', 'status', 'is_active')

from django.contrib import admin
from main.models import Experience,ExperienceImage,Organization

class ExperienceImageInline(admin.TabularInline):
    model = ExperienceImage
    extra = 35

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceImageInline]
    list_display = ('title', 'category', 'is_ongoing')

admin.site.register(Organization)

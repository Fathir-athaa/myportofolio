import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class ExperienceImage(models.Model):
    experience = models.ForeignKey(Experience, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='experiences/gallery/')

    def __str__(self):
        return f"Foto untuk {self.experience.title}"

class Organization(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Active Member")
    is_active = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    @property
    def is_ongoing(self):
        return self.is_active

class OrganizationImage(models.Model):
    organization = models.ForeignKey(Organization, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='organization_images/')

    def __str__(self):
        return f"Image for {self.organization.name}"

#test
#gua
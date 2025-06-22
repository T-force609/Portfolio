from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'post/{filename}'.format(filename=filename)


class Project(models.Model):
    Project_Type = (
        ('ML', 'Machine Learning'),
        ('Blender', '3D Art'),
        ('APP', 'Andriod App'),
        ('WEB', 'Web development'),
    )
    title  = models.CharField(max_length=200)
    project_type = models.CharField(max_length=7, choices=Project_Type)
    description = models.TextField()
    image = models.ImageField(_('Image'), upload_to=upload_to, blank=True)
    video = models.FileField(upload_to="videos/", blank=True)
    link = models.URLField(blank=True)
    source_code_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=50)
    category = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
    


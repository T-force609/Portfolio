from django.contrib import admin
from .models import Project, Skill

@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']
    list_filter = ['project_type', 'title', ]
    search_fields = ['title', 'project_type']

    


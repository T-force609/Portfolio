from django.db import models

class ContactRequest(models.Model):
    PROJECT_TYPE = (
        ('ML', 'Machine Learning'),
        ('3D', 'blender'),
        ('WEB', 'Web development'),
        ('APP', 'andriod app')
    )
    name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=10, choices=PROJECT_TYPE, default='Web Development')
    project_details = models.TextField()
    email = models.EmailField()
    budget = models.CharField(max_length=50, blank=True)
    deadline = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} - {self.get_request_type_display()}"

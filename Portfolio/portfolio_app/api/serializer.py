from rest_framework import serializers
from ..models import Project, Skill
from contact.models import ContactRequest

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'project_type', 'description', 'image', 'video', 'link', 'source_code_url']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = "__all__"
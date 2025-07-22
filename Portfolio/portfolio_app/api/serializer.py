from rest_framework import serializers
from ..models import Project, Skill
from contact.models import ContactRequest

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'project_type', 'description', 'image', 'video', 'link', 'source_code_url']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = '__all__'
    
    def validate(self, data):
        # Add custom validation if needed
        if len(data.get('project_details', '')) < 10:
            raise serializers.ValidationError("Project details must be at least 10 characters")
        return data

# In your viewset
def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {
                "status": "error",
                "errors": serializer.errors,
                "message": "Validation failed"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

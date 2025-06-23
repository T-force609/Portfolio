from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .api.serializer import ProjectSerializer, SkillSerializer, ContactMeSerializer
from .models import Project, Skill
from contact.models import ContactRequest
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ContactRequestView(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Process your data here
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list (self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)})

class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    #serializer_class = ProjectSerializer
    lookup_field = 'id'

    def get(self, request, id):
        try:
            project = get_object_or_404(Project, id=id)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

class SkillListView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    lookup_field = 'id'

class AdminPostUpload(APIView):
    parser_class = [MultiPartParser, FormParser]

    def Post(sef, request, format=None):
        print(request.data)
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ContactRequestViewSet(viewsets.ModelViewSet):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactMeSerializer
    http_method_name = ['post']

    def create(self, request, *arg, **kwarg):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        self.send_notification_email(serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "your request has been submitted successfully"},
            status= status.HTTP_201_CREATED,
            headers=headers
        )
    
    def send_notification_email(self, contact_request):
        subject = f"New Contact Request: {contact_request.name}"
        message = f"""
        You have a new contact request

        Name: {contact_request.name}
        Email: {contact_request.email}
        Request_Type: {contact_request.get_type_display()}
        Project Detail: {contact_request.project_details}
        Budget: {contact_request.deadline or 'Not specified'}
        Deadline: {contact_request.deadline or 'not specified'}
        """
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )



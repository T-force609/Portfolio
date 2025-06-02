from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from .api.serializer import ProjectSerializer, SkillSerializer, ContactMeSerializer
from .models import Project, Skill
from contact.models import ContactRequest
from django.core.mail import send_mail
from django.conf import settings

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillListView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

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



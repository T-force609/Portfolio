from django.shortcuts import render
from .models import ContactRequest
from portfolio_app.api.serializer import ContactMeSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

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
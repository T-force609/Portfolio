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
    serializer_class = ContactRequestSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_notification_email(instance)
    
    def send_notification_email(self, contact_request):
        subject = f"New Contact Request from {contact_request.name}"
        message = f"""
        New contact request received:
        
        Name: {contact_request.name}
        Email: {contact_request.email}
        Subject: {contact_request.subject}
        Message: {contact_request.message}
        """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.ADMIN_EMAIL]  # Make sure this is set in settings.py
        
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )

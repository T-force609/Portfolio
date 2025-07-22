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
    http_method_names = ['post']
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {
                    "status": "error",
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            self.perform_create(serializer)
            self.send_notification_email(serializer.instance)
            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

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
            request_type,
            project_detail,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )

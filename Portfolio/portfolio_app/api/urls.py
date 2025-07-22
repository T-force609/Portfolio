from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .. import views
from contact.views import ContactRequestViewSet
from ..views import (SkillListView, 
                     SkillDetialView, 
                     ProjectDetailView, 
                     ProjectListView, 
                     AdminPostUpload,)

router = DefaultRouter()
router.register(r'contact_request', ContactRequestViewSet, basename='contact_request')





urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skills_list'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('skills/<int:id>/', SkillDetialView.as_view(), name='skills_detail'),
    path('projects/<int:id>/', ProjectDetailView.as_view(), name='project_detail'),
    path('imagefiles/', AdminPostUpload.as_view(), name='imagefiles'),
    ]

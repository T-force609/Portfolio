from django.urls import path
from .. import views
from ..views import (SkillListView, 
                     SkillDetialView, 
                     ProjectDetailView, 
                     ProjectListView, 
                     AdminPostUpload,
                     ContactRequestViewSet)

urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skills_list'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('skills/<int:pk>/', SkillDetialView.as_view(), name='skills_detail'),
    path('projects/<int:id>/', ProjectDetailView.as_view(), name='project_detail'),
    path('imagefiles/', AdminPostUpload.as_view(), name='imagefiles'),
    path('contactrequests/', ContactRequestViewSet.as_view({'post': 'create'})),
    path('contact_request/', views.ContactRequestView, name='contact_request'),
]
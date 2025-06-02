from django.urls import path
from ..views import (SkillListView, 
                     SkillDetialView, 
                     ProjectDetailView, 
                     ProjectListView, 
                     AdminPostUpload,
                     ContactMeSerializer)

urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skills_list'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('skills/<int:pk>/', SkillDetialView.as_view(), name='skills_detail'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('imagefiles/', AdminPostUpload.as_view(), name='imagefiles'),
]
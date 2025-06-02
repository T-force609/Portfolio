from django.urls import path
from .views import SkillListView, SkillDetialView, ProjectDetailView, ProjectListView, ContactRequestViewSet
app_name = 'portfolio_app'

urlpatterns = [
    path('contact-requests/', ContactRequestViewSet.as_view({'post': 'create'})),
]
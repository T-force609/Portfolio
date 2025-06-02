from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Create your views here.

@login_required
def dashboard(request):
    context = {'page_title': 'Dashboard'}
    return render(request, 'custom_admin/dashboard.html', context)

class CustomLoginView(LoginView):
    template_name = 'admin/custom_admin/login.html'
    #authentication_form = CustomAuthForm
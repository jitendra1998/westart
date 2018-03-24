from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import StartUps

# Create your views here.
def index(request):
	return render(request, 'dashboard/landingpage.html')


def signup(request):
	return render(request, 'dashboard/signup.html')

def dashboard(request):
	return render(request, 'dashboard/dashboard.html')


def login(request):
	return render(request, 'dashboard/login.html')

class StartUpListView(ListView):
    queryset= StartUps.objects.all()
    template_name = 'dashboard/startups.html'

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
]

def home(request):
    return render(request, 'home.html', {})
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('login/', views.loginUser, name = 'Login'),
     path('logout', views.logoutUser, name = 'Logout'),
     path('register/', views.registerUser, name = 'Register'),
]

def home(request):
    return render(request, 'home.html', {})
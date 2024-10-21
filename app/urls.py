from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('login/', views.loginUser, name = 'Login'),
    # path('logout', views.logoutUser, name = 'Logout'),
]

def home(request):
    return render(request, 'home.html', {})
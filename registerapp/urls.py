from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('blog/', views.home, name='home'),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('userView/', views.userView, name='myresume'),
    path('createResume/', views.createResume, name='createResume'),
    path('accountSettings/', views.accountSettings, name='settings')
]

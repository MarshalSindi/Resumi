from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate,login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import CreateUserForm, PersonForm 
from .decorators import unauthenticated_user, admin_only, allowed_users
from .models import *
# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='candidat')
            user.groups.add(group)
            Person.objects.create(
                user=user,
                fullname=user.username
            )
            messages.success(request, 'Account Created for ' + username )
            return redirect('login')
    context = {'form':form}
    return render(request, 'myresume/register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Your Password OR Username is incorrect') 
    context = {}
    return render(request, 'myresume/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    context = {}
    return render(request, 'myresume/dashboard.html', context)

@login_required(login_url='login')
def createResume(request):
    context = {}
    return render(request, 'myresume/createResume.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles="candidat")
def userView(request):
    educations = request.user.person.education_set.all()
    experiences = request.user.person.experience_set.all()
    interests = request.user.person.interest_set.all()
    context = {'educations':educations, 'experiences':experiences, 'interests':interests}
    return render(request, 'myresume/myresume.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles="candidat")
def accountSettings(request):
    person = request.user.person
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'myresume/settings.html', context)
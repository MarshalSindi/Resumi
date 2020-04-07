from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate,login, logout
from django.contrib import messages
from .forms import CreateUserForm 
from .models import *
# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Created for ' + username )
            return redirect('login')
    context = {'form':form}
    return render(request, 'myresume/register.html',context)


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

def home(request):
    context = {}
    return render(request, 'myresume/dashboard.html', context)

def userView(request,pk):
    person = Person.objects.get(id=pk)
    educations = person.education_set.all()
    experiences = person.experience_set.all()
    interests = person.interest_set.all()
    context = {'person':person, 'educations':educations, 'experiences':experiences, 'interests':interests}
    return render(request, 'myresume/user.html', context)
from django.shortcuts import render
import requests
from datetime import date
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def achievements(request):
    return render(request, 'achievements.html', {})

def technology(request):
    return render(request, 'technology.html', {})
    
def apod(request):
    if request.POST.get('date'):
        dateuser = request.POST.get('date')
    else:
        today= date.today()
        year = today.year
        month = today.month
        day = today.day
        dateuser = f'{year}-{month}-{day}'
    
    url = 'https://api.nasa.gov/planetary/apod'
    r=requests.get(url, params={"api_key": 'lnjLOPvbSjjy8fBS3tHsUHtlD3qBigaxUfQe8gUW', "date": dateuser}).json()
    imginfo= {
    'date':r['date'],
    'explanation':r['explanation'],
    'hdurl':r['hdurl']
    }
    print(imginfo)
    context={'imginfo':imginfo}
    return render(request, 'apod.html', context)

def contact(request):
    return render(request, 'join us.html', {})
    
def about(request):
    return render(request, 'about us.html', {})


def signupaccount(request):
    if request.method == "GET":
        return render(request, "signupaccount.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("login")
            except IntegrityError:
                return render(
                    request,
                    "signupaccount.html",
                    {"form": UserCreationForm, "error": "Username already taken"},
                )
        else:
            return render(
                request,
                "signupaccount.html",
                {"form": UserCreationForm, "error": "Password didn't match"},
            )


def logoutaccount(request):
    logout(request)
    return redirect("login")


def loginaccount(request):
    if request.method == "GET":
        return render(request, "loginaccount.html", {"form": AuthenticationForm})

    else:
        User = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if User is None:
            return render(
                request,
                "loginaccount.html",
                {
                    "form": AuthenticationForm,
                    "error": "Username and password didn't match",
                },
            )
        else:
            login(request, User)
            return render(request, "index.html", {})
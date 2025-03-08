import subprocess
import sys
from django.http import JsonResponse
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout





yoga_process = None



def start_yoga(request):
    global yoga_process  
    try:
       
        python_executable = r'D:/M/yoga_web/MP/yoga/env/Scripts/python.exe'

       
        yoga_process = subprocess.Popen(
            [python_executable, 'D:/M/yoga_web/MP/yoga/live_detection.py'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        return JsonResponse({'status': 'success', 'message': 'Yoga session started.'})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def stop_yoga(request):
    global yoga_process  
    try:
        if yoga_process and yoga_process.poll() is None:  
            yoga_process.terminate()  
            yoga_process = None  
            return JsonResponse({'status': 'success', 'message': 'Yoga session stopped.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No active yoga session to stop.'})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  
            user.save()
            return redirect("login")  
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "registration/login.html", {"error": "Invalid username or password"})

    return render(request, "registration/login.html")
       



def logout_view(request):
    logout(request)
    return redirect("home")

def home(request):
    return render(request, 'homepage.html')

def contact(request):
    return render(request, 'contact.html')

def learn(request):
    return render(request, 'learn.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')  
def poses(request):
    return render(request, 'poses.html')

def start_pose(request):
    return render(request, 'start_pose.html')
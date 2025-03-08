from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('/pose_checker/')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pose_checker/', include('pose_checker.urls')),
    path('', home_redirect),  
]

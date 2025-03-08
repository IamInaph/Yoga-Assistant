from django.urls import path, include
from .views import home, register, login_view,logout_view,about, start_yoga, stop_yoga

from . import views  


urlpatterns = [
    path('', home, name='home'),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('start-yoga/', start_yoga, name='start_yoga'),  
    path('stop-yoga/', stop_yoga, name='stop_yoga'),    

    path('contact/', views.contact, name='contact'),
    path('learn/', views.learn, name='learn'),
    path('about/', views.about, name='about'),

    path('poses/', views.poses, name='poses'),

    path('start_pose/', views.start_pose, name='start_pose'),
]
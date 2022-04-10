from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index') # Connect to project-level urls.py
]
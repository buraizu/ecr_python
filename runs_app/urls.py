from django.urls import path
from . import views

urlpatterns = [
    path('<topic>/', views.runs_view, name='runs-page')
]
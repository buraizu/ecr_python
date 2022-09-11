from django.urls import path
from . import views

# register the app namespace
app_name = 'runs_app'

urlpatterns = [
    path('', views.list_runs, name='list_runs'),
    path('run/', views.run_detail, name='run_detail'),
    path('add_run/', views.add_run, name='add_run'),
]

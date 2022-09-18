from django.urls import path
from .views import RunCreateView, RunListView
from . import views

# register the app namespace
app_name = 'runs_app'

urlpatterns = [
    path('list_runs', RunListView.as_view(), name='list_runs'),
    path('run/', views.run_detail, name='run_detail'),
    path('create_run/', RunCreateView.as_view(), name='create_run')
]

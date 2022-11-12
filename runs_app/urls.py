from django.urls import path
from .views import RunCreateView,RunListView,RunDetailView,RunUpdateView,RunDeleteView
from . import views

# register the app namespace
app_name = 'runs_app'

urlpatterns = [
    path('list_runs/', RunListView.as_view(), name='list_runs'),
    path('create_run/', RunCreateView.as_view(), name='create_run'),
    path('run_detail/<int:pk>/', RunDetailView.as_view(), name='run_detail'),
    path('update_run/<int:pk>/', RunUpdateView.as_view(), name='update_run'),
    path('delete_run/<int:pk>/', RunDeleteView.as_view(), name='delete_run')
]

from django.urls import path
from .views import RunnerEventCreateView
from . import views

app_name = 'runner_events_app'

urlpatterns = [
    path('create_runner_event/', RunnerEventCreateView.as_view(), name='create_runner_event')
]
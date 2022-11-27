from django.urls import path
from .views import RunnerEventCreateView, RunnerEventListView
from . import views

app_name = 'runner_events_app'

urlpatterns = [
    path('create_runner_event/', RunnerEventCreateView.as_view(), name='create_runner_event'),
    path('list_runner_events/', RunnerEventListView.as_view(), name='list_runner_events')
]
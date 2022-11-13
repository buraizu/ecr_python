from django.urls import path
from .views import EventListView
from . import views

app_name = 'events_app'

urlpatterns = [
    path('list_events', EventListView.as_view(), name='list_events')
]
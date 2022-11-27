from django.urls import path
from .views import EventListView, EventDetailView
# from . import view

app_name = 'events_app'

urlpatterns = [
    path('list_events', EventListView.as_view(), name='list_events'),
    path('event_detail/<int:pk>', EventDetailView.as_view(), name='event_detail')
]
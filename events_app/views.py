from django.shortcuts import render
from django.views.generic import ListView
from events_app.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class EventListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = "event_list"
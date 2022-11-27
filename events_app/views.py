from django.shortcuts import render
from django.views.generic import ListView, DetailView
from events_app.models import Event
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class EventListView(ListView):
    model = Event
    context_object_name = "event_list"

class EventDetailView(DetailView):
    model = Event

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
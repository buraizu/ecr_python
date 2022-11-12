from django.shortcuts import render
from django.views.generic import ListView
from events_app.models import Event, UserEvent
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class EventListView(ListView):
    model = Event
    context_object_name = "event_list"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserEventCreateView(CreateView):
    model = UserEvent
    fields = ['goal_time']

    def form_valid(self, form):
        form.instance.x = self.request.x

        return super().form_valid(form)

    success_url = reverse_lazy('events_app:list_events')
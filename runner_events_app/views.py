from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RunnerEvent

# Create your views here.
class RunnerEventCreateView(CreateView, LoginRequiredMixin):
    model = RunnerEvent
    fields = ['goal_time']

    # def form_valid(self, form):
    #     form.instance.runner = self.request.user
        # form.instance.event = 
        # return super().form_valid(form)
        
    # success_url = reverse_lazy('runs_app:list_runs')

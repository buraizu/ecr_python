from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from runs_app.models import Run
from .forms import AddRunForm
from . import models

# Create your views here.

class RunsView(TemplateView):
    template_name = 'runs_app/runs.html'

class RunCreateView(CreateView):
    model = Run
    fields = "__all__"
    success_url = reverse_lazy('runs_app:list_runs')

class RunListView(ListView):
    model = Run
    context_object_name = "run_list"

class RunDetailView(DetailView):
    model = Run

class RunUpdateView(UpdateView):
    model = Run
    fields = "__all__"
    success_url = reverse_lazy('runs_app:list_runs')

class RunDeleteView(DeleteView):
    model = Run
    success_url = reverse_lazy('runs_app:list_runs')

# class RunFormView(FormView):
#     form_class = AddRunForm
#     template_name = 'runs_app/add_run.html'

#     success_url = reverse_lazy('runs_app:list_runs')

#     def form_valid(self,form):
#         print(form.cleaned_data)
#         return super().form_valid(form)

# def list_runs(request):

#     all_runs = models.Run.objects.all()
#     context = {'runs':all_runs}

#     return render(request, 'runs_app/runs.html', context=context)

def run_detail(request):

    my_var = {'first_name': 'first', 'last_name': 'last',
        'some_list': [1,2,3], 'user_logged_in': True
    }
    return render(request, 'runs_app/run.html', context = my_var)

def add_run(request):

    # POST REQUEST --> FORM CONTENTS --> LIST RUNS
    if request.method == 'POST':
        form = AddRunForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('runs_app:list_runs'))

    # ELSE, RENDER FORM
    else:
        form = AddRunForm()
    return render(request, 'runs_app/add_run.html', context={'form':form})


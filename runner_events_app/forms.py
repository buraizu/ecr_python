from django.forms import ModelForm
from .models import RunnerEvent


class AddRunnerEventForm(ModelForm):
    class Meta:
        model = RunnerEvent
        fields = ['goal_time']

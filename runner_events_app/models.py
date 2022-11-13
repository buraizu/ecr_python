from django.db import models
from django.urls import reverse, reverse_lazy
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
import uuid

# Create your models here.
class RunnerEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey('events_app.Event', on_delete=models.PROTECT)
    runner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    goal_time = models.IntegerField(validators=[MinValueValidator(1)])
    result_time = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)

    # def get_absolute_url(self):
    #     return reverse("user_event_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.event.name} on {self.event.date}!"
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
import uuid

class Event(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField()
    description = models.TextField()
    event_home_url = models.URLField()
    event_registration_url = models.URLField()

    def __str__(self):
        return f"{self.name} on {self.date}."

class UserEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey('Event', on_delete=models.PROTECT)
    goal_time = models.IntegerField(validators=[MinValueValidator(1)])
    result_time = models.IntegerField(validators=[MinValueValidator(1)])

    def get_absolute_url(self):
        return reverse("user_event_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.user}'s {self.event.name} on {self.event.date}!"
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField()
    description = models.TextField()
    event_home_url = models.URLField()
    event_registration_url = models.URLField()

    def __str__(self):
        return f"{self.name} on {self.date}."

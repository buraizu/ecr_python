from django.db import models

# Create your models here.
class Run(models.Model):
    course = models.CharField(max_length=80)
    distance = models.IntegerField()
    time = models.IntegerField()
    rating = models.IntegerField()
    review = models.TextField()
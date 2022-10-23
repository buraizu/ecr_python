from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Run(models.Model):
    course = models.CharField(max_length=80)
    distance = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    review = models.TextField()

    def __str__(self):
        return f"{self.course} with a distance of {self.distance} and a time of {self.duration}. The rating is {self.rating} and the review is {self.review}."
    
    def get_absolute_url(self):
        return reverse("run_detail", kwargs={"pk": self.pk})
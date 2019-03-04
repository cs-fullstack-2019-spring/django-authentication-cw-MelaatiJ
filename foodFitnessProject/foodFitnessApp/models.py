from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# username, calories, and date.
class FoodFitnessModel(models.Model):
    userName = models.CharField(max_length=200, default="")
    calorie = models.IntegerField(default=0)
    date = models.DateField(default="")
    foodFitnessForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.userName

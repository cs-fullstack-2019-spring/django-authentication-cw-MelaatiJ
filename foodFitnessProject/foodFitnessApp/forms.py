from .models import FoodFitnessModel
from django import forms

class FoodFitnessForm(forms.ModelForm):
    class Meta:
        model= FoodFitnessModel
        exclude = ["foodFitnessForeignKey"]
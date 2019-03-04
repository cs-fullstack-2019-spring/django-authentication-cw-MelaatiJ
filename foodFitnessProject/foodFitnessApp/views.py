from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import FoodFitnessModel, FoodFitnessForm
from django.contrib.auth.models import User


# Create your views here.
#function renders to the index page
def index(request):
    return render(request, "foodFitnessApp/index.html")

#function adds a new user and renders to the add user page
def addUser(request):
    form = FoodFitnessForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request, "foodFitnessApp/addUser.html", context)

#my function that prints the post made and create a new user in the admin . once submitted it will post the httpresponse
# listed
def info(request):
    print(request.POST)
    User.objects.create_user(request.POST["userName"], "", "")

    return HttpResponse("you gonna be skinny")

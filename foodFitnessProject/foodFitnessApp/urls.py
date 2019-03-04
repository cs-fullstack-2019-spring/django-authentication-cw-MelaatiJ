from django.urls import path
from . import views

#my url end points
# one end point that leads to the index that asks you to create a user
#second end point adds a user and saves it into the admin
# third send you to a new page oce submitted
urlpatterns = [
    path("", views.index, name="index"),
    path("addUser/", views.addUser, name="addUser"),
    path("info/", views.info, name="info"),

]

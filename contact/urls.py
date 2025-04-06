from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_contact, name="contact"),
    path("/complaint", views.compaint, name="complaint"),

]
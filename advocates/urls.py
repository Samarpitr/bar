from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_advocates, name="list_advocates"),
]
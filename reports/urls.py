from . import views
from django.urls import path

urlpatterns = [
    path("", views.reports, name="reports"),
    path("records", views.records, name="records"),
]

from . import views
from django.urls import path

urlpatterns = [
    path("", views.list_services, name="list_services"),
    path("service/<int:service_id>/", views.service_detail, name="service_detail"),
]

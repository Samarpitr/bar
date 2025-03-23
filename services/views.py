from django.shortcuts import render
from .models import Service

def list_services(request):
    services = Service.objects.all()
    return render(request, 'list_services.html', context={"services": services})

def service_detail(request, service_id):
    service = Service.objects.get(id=service_id)
    return render(request, 'service_detail.html', context={"service": service})
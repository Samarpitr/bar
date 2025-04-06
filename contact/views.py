from django.shortcuts import render
from .models import ContactUs


def list_contact(request):
    contact = ContactUs.objects.first()
    return render(request, 'contact_us.html', context={"contact": contact})


def compaint(request):
    contact = ContactUs.objects.first()
    return render(request, 'complaint.html', context={"contact": contact})
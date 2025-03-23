from django.shortcuts import render
from .models import Notice


def list_notice(request):
    notices = Notice.objects.all().order_by('-created_at')[0:12]
    return render(request, 'list_notices.html', context={"notices": notices})
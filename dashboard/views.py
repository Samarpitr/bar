from django.http.response import HttpResponse
from django.shortcuts import render
from notice.models import Notice
from .models import Banner
from advocates.models import Advocate, AdvocateRole
from officer.models import Officers
from datetime import datetime

def dashboard(request) -> HttpResponse:
    notices = Notice.objects.filter(is_active=True).order_by('-created_at')[:12]
    banners = Banner.objects.all()
    current_year = datetime.now().year
    members = AdvocateRole.objects.filter(appointed_on__year=current_year).order_by('appointed_on')
    officers = Officers.objects.all().order_by('rank')
    return render(request, 'dashboard.html', context={'notices': notices, 'banners': banners, 'members': members, 'officers': officers})


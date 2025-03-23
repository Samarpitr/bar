from django.shortcuts import render
from .models import Advocate, AdvocateRole


def list_advocates(request):
    advocates = Advocate.objects.all().order_by('advocaterole__appointed_on')
    return render(request, 'list_advocates.html', context={"advocates": advocates})
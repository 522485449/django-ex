import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')

    PageView.objects.create(hostname=hostname)
    PageView(hostname='3').save()
    for pageview in (PageView.objects.all()):
        open(r'welcome\templates\welcome\index.html','a').write('<p/>'+pageview.__str__())

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

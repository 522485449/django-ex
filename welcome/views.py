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
    string=''
    for pageview in (PageView.objects.all()):
        open(r'welcome\templates\welcome\index.html','a').write('<p/>'+pageview.__str__())
        string+=pageview.__str__()+'\r\n     <p/>'
    # return render(request, 'welcome/index.html', {
    #     'hostname': hostname,
    #     'database': database.info(),
    #     'count': PageView.objects.count()
    # })
    return HttpResponse("Hello NowaMagic"+string)

def health(request):
    return HttpResponse(PageView.objects.count())

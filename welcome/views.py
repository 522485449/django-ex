import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import logging
from . import database
from .models import PageView,Preference

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


def database_tool(request):
    #action='selectAll'
    #database='webPageView'
    rmap=request.GET
    action=rmap.get('action')[0].lower()
    database=rmap.get('database')[0].lower()
    print('action:%s,database:%s'%(action,database))

    Preference(key='kay3455555555555',value='value3').save()
    if action!='selectall':
        if database!='preference':
            string=''
            string+='<tr><th>id</th><th>key</th><th>value</th><th>timestamp</th></tr>'
            for pre in (Preference.objects.all()):
                string+='<tr><td>%i</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(pre.id,pre.key,pre.value,str(pre.timestamp))
            string='<html><body><table border="1">%s</table></body></html>'%string
            return HttpResponse(string)



    #{'gh': ['39']}

    logger = logging.getLogger('test1')
    logger.error('Something went wrong!')
    return HttpResponse(PageView.objects.count())
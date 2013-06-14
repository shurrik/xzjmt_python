# coding=utf-8
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    #return render_to_response('index.html',{'name':'oh'},context_instance=RequestContext(request))
    c = RequestContext(request, {
    'name': 'lipeng',
    })
    return render_to_response('home.html',c)


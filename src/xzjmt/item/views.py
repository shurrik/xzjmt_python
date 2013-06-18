# coding=utf-8
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from xzjmt.item.models import Item

curNav = 'item'

def list(request):
    items = Item.objects.all()
    c = RequestContext(request, {
      'items':items,
      'curNav':curNav,                           
    })
    return render_to_response('item/list.html',c)

def detail(request,id):
    print id
    c = RequestContext(request, {
    'self':False,
    'curNav':curNav,
    })
    return render_to_response('item/detail.html',c)

# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

@login_required
def index(request):
    c = RequestContext(request, {
    })
    return render_to_response('self/index.html',c)

@login_required
def newItem(request):
    c = RequestContext(request, {
    })
    return render_to_response('self/item.html',c)

@login_required
def listItem(request):
    c = RequestContext(request, {
    })
    return render_to_response('self/item_list.html',c)

@login_required
def delItem(request,id):
    c = RequestContext(request, {
    })
    return HttpResponseRedirect("/self/item/list")

@login_required
def addItem(request):
    c = RequestContext(request, {
    })
    return HttpResponseRedirect("/self")

@login_required
def profile(request):
    c = RequestContext(request, {
    })
    return render_to_response('self/profile.html',c)

@login_required
def save(request):
    c = RequestContext(request, {
    })
    return HttpResponseRedirect("/self")

@login_required
def write(request,usrId):
    c = RequestContext(request, {
    })
    return render_to_response('self/message/write.html',c)

@login_required
def send(request):
    c = RequestContext(request, {
    })
    return HttpResponseRedirect("/self")

@login_required
def listMessage(request):
    c = RequestContext(request, {
    })
    return render_to_response('self/message/list.html',c)

@login_required
def messageDetail(request,id):
    c = RequestContext(request, {
    })
    return render_to_response('self/message/detail.html',c)

@login_required
def replyMessage(request,id):
    c = RequestContext(request, {
    })
    return render_to_response('self/message/reply.html',c)

@login_required
def follow(request,usrId):
    c = RequestContext(request, {
    })
    return 'succ'

@login_required
def collect(request,itemId):
    c = RequestContext(request, {
    })
    return 'succ'

@login_required
def collection(request):
    c = RequestContext(request, {
    })
    return render_to_response('self/collection.html',c)

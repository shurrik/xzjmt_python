# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template.context import RequestContext

@login_required
def index(request):
    c = RequestContext(request, {
    })
    return render_to_response('self/index.html',c)

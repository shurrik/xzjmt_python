# coding=utf-8
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User# Create your views here.


def reg(request):
    c = RequestContext(request, {
    })
    return render_to_response('reg/input.html',c)

def save(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username=username,email=email,password=password)
    user.save()
    c = RequestContext(request, {
    })
    return render_to_response('reg/succ.html',c)

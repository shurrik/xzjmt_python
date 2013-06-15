# coding=utf-8
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    curNav = 'home'
    c = RequestContext(request, {
    'curNav':curNav,
    })
    return render_to_response('home.html',c)

def about(request):
    curNav = 'about'
    c = RequestContext(request, {
    'curNav':curNav,
    })
    return render_to_response('about.html',c)

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/")
    else:
        # Show an error page
        return HttpResponseRedirect("/")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def accountLogin(request):
    n = request.GET.get('next', '')
    c = RequestContext(request, {
    'next':n,
    })
    return render_to_response('login_view.html',c)

def accountAuth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    n = request.POST.get('next', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect(n)
    else:
#         c = RequestContext(request, {
#         'next':n,
#         })
#         return render_to_response('login_view.html',c)
        return HttpResponseRedirect('/accounts/login/?next='+n)
    
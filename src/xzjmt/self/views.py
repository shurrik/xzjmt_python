# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from xzjmt import item
from xzjmt.category.models import Category
from xzjmt.city.models import City
from xzjmt.item.models import Item
from xzjmt.itempic.models import ItemPic
import datetime

@login_required
def index(request):
    c = RequestContext(request, {
    })
    return render_to_response('self/index.html',c)

@login_required
def newItem(request):
    citys = City.objects.all()
    categorys = Category.objects.all()
    c = RequestContext(request, {
    'citys':citys,
    'categorys':categorys,                                
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
    picUrls = request.POST.getlist('picUrl')
    picUrlSmalls = request.POST.getlist('picUrlSmall')
    user = request.user
    name = request.POST.get('name', '')
    desc = request.POST.get('desc', '')
    picCover = request.POST.get('picCover', '')
    cityId = request.POST.get('cityId', '')
    catId = request.POST.get('catId', '')
    
    item = Item(name = name,
                item_desc = desc,
                pic_cover = picCover,
                cat_id = catId,
                city_id = cityId,
                user_id = user.id,
                email = user.email,
                nick_name = user.username,
                create_date = datetime.datetime.now()
                )
    item.save()
    
    for picUrl in picUrls:
        itemPic = ItemPic(itemid = item.item_id,
                          pic_url = picUrl,
                          create_date = datetime.datetime.now()
                          )
        itemPic.save()
    
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

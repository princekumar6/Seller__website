from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from seller.models import New_sup,Products
from .models import Discussion,Comment

def forum(request):
    obj = Discussion.objects.all().order_by('-date')
    return render(request,'forum/forum.html',{'data':obj})

def disc(request,prod):
    data = Discussion.objects.get(dis_id=prod)
    data1 = Comment.objects.filter(dis_id=prod).order_by('-date')
    return render(request,'forum/disc.html',{'data':data,'data1':data1})

def newdis(request):
    if request.session.get('sup_id'):
        return render(request,'forum/new-dis.html')
    else:
        return redirect('/register/')

def addnew(request):
    o = New_sup.objects.get(sup_id=request.session.get('sup_id'))
    data = {
        'topic' : request.POST.get('topic'),
        'content' : request.POST.get('content'),
        'name' : o.name,
        'last' : o.name,
    }
    obj = Products.objects.get(na='Prods')
    data['dis_id'] = f'id{str(obj.discussid)}'
    nobj = Discussion.objects.create(**data)
    nobj.save()
    obj.discussid += 1
    obj.save()

    return redirect('/forum/')

def cmnt(request,prod):
    if request.session.get('sup_id'):
        obj = Discussion.objects.get(dis_id=prod)
        return render(request,'forum/new-com.html',{'data':obj})
    else:
        return redirect('/register/')

def addnewc(request,prod):
    o = New_sup.objects.get(sup_id=request.session.get('sup_id'))
    data = {
        'content' : request.POST.get('content'),
        'name' : o.name,
        'dis_id' : Discussion.objects.get(dis_id=prod),
    }
    nobj = Comment.objects.create(**data)
    nobj.save()
    obj = Discussion.objects.get(dis_id=prod)
    obj.cmnt += 1
    obj.save()
    return redirect('/forum/')
   


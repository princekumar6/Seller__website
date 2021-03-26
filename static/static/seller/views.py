from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import New_sup, Bank_verify, Entity_verify, Representative_verify

def admin(request):
    return render(request,'seller/admin-login.html')

def verify(request):
    pswd = request.POST.get('pass')
    if pswd == 'Aditya@details':
        return render(request,'seller/admin-panel.html')
    else:
        return redirect('/seller/admin/')

def emailsend(request):
    to_email = request.POST.get('email')
    op = request.POST.get('em')
    html_content = render_to_string(f'email{op}.html')
    text_content = strip_tags(html_content)

    if op=="1":ms="Seventh Square Email Verification"
    elif op=="2":ms="Welcome To Seventh Square!"
    elif op=="3":ms="Sell on India's first Home Products Marketplace"
    elif op=="4":ms="Seventh Square Account Verification"

    email = EmailMultiAlternatives(
        ms,
        text_content,
        settings.EMAIL_HOST_USER,
        [to_email]
    )
    email.attach_alternative(html_content,'text/html')
    email.send()
    return render(request,'seller/admin-panel.html')

def sellerid(request):
    sid = request.POST.get('id')
    data = New_sup.objects.get(sup_id=sid)
    try:
        data1 = Bank_verify.objects.get(sup_id=sid)
        data2 = Entity_verify.objects.get(sup_id=sid)
        data3 = Representative_verify.objects.get(sup_id=sid)
        
    except:pass
    finally:return render(request,'seller/admin-details.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})

# def details(request):

    
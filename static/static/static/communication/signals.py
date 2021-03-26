from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from.models import Notification
from django.shortcuts import redirect,render,request
from django.contrib import messages

@receiver(post_save,sender=User)
def send_notification(sender,instance,created,**kwargs):
    if kwargs.get(created,False):
        Notification.objects.create(user=kwargs.get('instance'),message='Registration is successfull Thanks for Registering')
       
        redirect(request,"account/login.html")
    
        
    else:
        return render(request,"account/register.html")
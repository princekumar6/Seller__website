import utility
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View

from .models import Account


class Register(View):
    template_name = 'account/register.html'

    def get(self,request,*args,**kwargs):
        return render(request,template_name=self.template_name)

    def post(self,request,*args,**kwargs):
        data = {
        'Representativename' : request.POST.get('Representativename'),
        'companyName' : request.POST.get('companyName'),
        'email' : request.POST.get('email'),
        'mobileNumber' : request.POST.get('mobileNumber'),
        'password' : request.POST.get('password'),
        'companyGSTNumber' : request.POST.get('companyGSTNumber'),
        }
        try:
            account=Account(**data)
            account.full_clean()
            redirect('account/login.html')
        except(IntegrityError):
            # mobile and email is unique
            message = "Either Email or Mobile Number is Already Registered !!"
            color = "danger"
            return render(request,self.template_name,{'message':message,'color':color})
        except(ValidationError):
            message = "Validation error!!"
            color = "danger"
            return render(request,self.template_name,{'message':message,'color':color,'error':ValidationError})

class Login(View):
    template_name = 'account/login.html'

    def get(self,request,*args,**kwargs):
        return render(request,template_name=self.template_name)

    def post(self,request,*args,**kwargs):
        return render(request,'login post')

class Forget(View):
    template_name = 'account/forget.html'

    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        pass

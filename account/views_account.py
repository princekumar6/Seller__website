import utility
from communication import communication
from django.contrib.auth import login, logout
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
        'username':request.POST.get('mobileNumber'),
        'Representativename' : request.POST.get('Representativename'),
        'companyName' : request.POST.get('companyName'),
        'email' : request.POST.get('email'),
        'mobileNumber' : request.POST.get('mobileNumber'),
        'password' : request.POST.get('password'),
        'companyGSTNumber' : request.POST.get('companyGSTNumber'),
        }
        try:
            account=Account(**data)
            account.set_password(data['password'])
            account.full_clean()
            account.save()

            # send email and mobile
            channels={
                'email':{
                    'to':[account.email],
                    'data': {
                        'mobile_otp' : account.mobileVerificationCode,
                        'user':account.id
                        },
                    'template' : 'register.html'},

                'mobile':{
                    'to':[account.mobileNumber],
                    'data': {
                        'email_otp' : account.emailVerificationCode,
                        'user':account.id
                        },
                    'template' : 'register.txt'
                    }

            }
            communication.send(channels)
            return redirect('/account/login')
        except(IntegrityError):
            # mobile and email is unique
            message = "Either Email or Mobile Number is Already Registered !!"
            color = "danger"
            return render(request,self.template_name,{'message':message,'color':color})
        except ValidationError as err:
            message = "Validation error!!"
            color = "danger"
            print(err.message_dict.items())
            return render(request,self.template_name,{'message':message,'color':color,'error':err})

class Login(View):
    template_name = 'account/login.html'
    def get(self,request,*args,**kwargs):
        print(request.user)
        return render(request,template_name=self.template_name)
    def post(self,request,*args,**kwargs):
        data={
            'email':request.POST.get('mobileNumber'),
            'mobileNumber' : request.POST.get('mobileNumber') 
        }
        password = request.POST.get('password') 
        try:
            account = Account.objects.get(Q(email=data['email'])| Q(mobileNumber=data['mobileNumber']))
            if account.check_password(password):
                login(request,account)
                return redirect('/')
            else:
                message='Password is incorrect'
                color = 'danger'
                return render(request,template_name=self.template_name,context={'color':color,'message':message})
        except ObjectDoesNotExist:
            message='The account does not exist. please enter a valid email/mobile number'
            color='danger'
            return render(request,template_name=self.template_name,context={'color':color,'message':message})
            
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('/account/login')

    def post(self,request):
        logout(request)
        return redirect('/account/login')

class Forget(View):
    template_name = 'account/login.html'

    def get(self,request,*args,**kwargs):
        return redirect('/account/login')
    def post(self,request,*args,**kwargs):
        data={
            'email':request.POST.get('mobileNumber'),
            'mobileNumber' : request.POST.get('mobileNumber') 
        }
        try:
            account = Account.objects.get(Q(email=data['email'])| Q(mobileNumber=data['mobileNumber']))
            verificationCode=utility.randomString(10)
            account.emailVerificationCode = verificationCode
            account.mobileVerificationCode = verificationCode
            account.save()
            channels={
                'email':{
                    'to':[account.email],
                    'data': {
                        'mobile_otp' : account.mobileVerificationCode,
                        'user':account.id
                        },
                    'template' : 'forget.html'
                },

                'mobile':{
                    'to':[account.mobileNumber],
                    'data': {
                        'email_otp' : account.emailVerificationCode,
                        'user':account.id
                        },
                    'template' : 'forget.txt'
                }

            }
            communication.send(channels)
            message='A password reset link is sended to your Email  and Mobile'
            color = 'info'
            return render(request,template_name=self.template_name,context={'color':color,'message':message})
        except ObjectDoesNotExist:
            message='The account does not exist. please enter a valid email/mobile number'
            color='danger'
            return render(request,template_name=self.template_name,context={'color':color,'message':message})
        
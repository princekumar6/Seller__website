from django.shortcuts import redirect, render
from django.views import View

from account.models import Account


class RepresentativeDetail(View):
    template_name=''
    def get(self,request,*args,**kwargs):
        return  redirect('/account/')
    def post(self,request):
        Representativename = request.POST.get('Representativename')
        mobileNumber = request.POST.get('mobileNumber')
        email = request.POST.get('email')
        password = request.POST.get('password')
        representativeimage = request.FILES.get('representativeimage')
        
        
        account = Account.objects.get(pk=request.user.id)
        
        if Representativename is not None and Representativename !='':
            account.Representativename = Representativename
        if mobileNumber is not None and mobileNumber !='':
            account.mobileNumber = mobileNumber
        if email is not None and email !='':
            account.email = email
        if password is not None and password !='':
            account.set_password(password)
        if representativeimage is not None and  representativeimage !='':
            account.Representativeimage = representativeimage
        try:
            account.save()
        except(Exception):
            print('exception___')
        return  redirect('/account/')

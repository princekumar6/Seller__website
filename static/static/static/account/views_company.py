from django.shortcuts import redirect, render
from django.views import View

from account.models import Account


class CompanyDetail(View):
    template_name=''
    def get(self,request,*args,**kwargs):
        return  redirect('/account/')
    def post(self,request):
        companyName = request.POST.get('companyName')
        addressCompany = request.POST.get('addressCompany')
        companyCategory = request.POST.get('companyCategory')
        companyAbout = request.POST.get('companyAbout')
        account = Account.objects.get(pk=request.user.id)
        
        if companyName !='':
            account.companyName = companyName
        if companyCategory !='':
            account.companyCategory = companyCategory
        if companyAbout !='':
            account.companyAbout = companyAbout
        try:
            account.save()
        except(Exception):
            pass
        print(request.POST,request.FILES)
        return  redirect('/account/')

from django.shortcuts import redirect, render
from django.views import View

from account.models import Account


class EntityDetail(View):
    template_name=''
    def get(self,request,*args,**kwargs):
        return  redirect('/account/')
    def post(self,request):
        companyGSTNumber = request.POST.get('companyGSTNumber')
        companyPAN = request.POST.get('companyPAN')
        companyKYCDocType = request.POST.get('companyKYCDocType')
        companyKYCDOC = request.FILES.get('companyKYCDOC')
        companyCIN = request.POST.get('companyCIN')
        account = Account.objects.get(pk=request.user.id)
        print(request.POST,request.FILES)
        
        if companyGSTNumber !='':
            account.companyGSTNumber = companyGSTNumber
        if companyPAN !='':
            account.companyPAN = companyPAN
        if companyKYCDocType !='':
            account.companyKYCDocType = companyKYCDocType
        if companyKYCDOC is not None and companyKYCDOC !='':
            account.companyKYCDOC = companyKYCDOC
        if companyCIN !='':
            account.companyCIN = companyCIN
        try:
            account.save()
        except(Exception):
            pass
        return  redirect('/account/')

from bank.models import Bank
from django.shortcuts import redirect, render
from django.views import View


class BankDetail(View):
    template_name=''
    def get(self,request,*args,**kwargs):
        return  redirect('/account/')
    def post(self,request):
        accountHolderName = request.POST.get('accountHolderName')
        accountNumber = request.POST.get('accountNumber')
        ifsc = request.POST.get('ifsc')
        bank = request.POST.get('bank')
        branch = request.POST.get('branch')
        print(request.POST)
        
        account,created = Bank.objects.get_or_create(account=request.user)
        
        if accountHolderName !='':
            account.accountHolderName = accountHolderName
        if accountNumber !='':
            account.accountNumber = accountNumber
        if ifsc !='':
            account.ifsc = ifsc
        if bank !='':
            account.bank = bank
        if branch !='':
            account.branch = branch
            
        try:
            account.save()
        except(Exception):
            pass
        return  redirect('/account/')

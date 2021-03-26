from address.models import Address
from bank.models import Bank
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from theseventhsquare.settings import MEDIA_URL

from account.models import Account


def Profile(request):
    account = Account.objects.get(pk=request.user.id)
    bank = Bank.objects.filter(account=request.user.id).first()
    
    addressCompany = Address.objects.filter(account=request.user,addressType='COMPANY').first()
    if addressCompany is None:
        addressCompany={} 
    addressRepresentative = Address.objects.filter(account=request.user,addressType='REPRESENTATIVE').first()
    if addressRepresentative is None:
        addressRepresentative={} 
    context={
        'account':account,
        'addressCompany':addressCompany,
        'addressRepresentative':addressRepresentative,
        'bank' : bank,
        'REPR_CHOICES':Account.REPR_CHOICES,
        'COMAPNY_CATEGORY':Account.COMAPNY_CATEGORY,
        'DOC_TYPE_CHOIES':Account.DOC_TYPE_CHOIES,
        'BANK_CHOICES':Bank.BANK_CHOICES,
        'STATE_CHOICES':Address.STATE_CHOICES,
        'media_url':MEDIA_URL
    }
    return render(request,template_name='account/profile.html',context=context)

def KYCDocFileDownload(request):
    pass

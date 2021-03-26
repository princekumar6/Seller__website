from address.models import Address
from django.shortcuts import redirect, render
from django.views import View


class AddressDetail(View):
    template_name=''
    def get(self,request,*args,**kwargs):
        return  redirect('/account/')
    def post(self,request):
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        account,created = Address.objects.get_or_create(pk=request.user.id,defaults={'account':request.user,'addressType':'COMPANY'})
        print(request.POST,request.FILES)
        
        if address !='':
            account.address = address
        if city !='':
            account.city = city
        if state !='':
            account.state = state
        if pincode is not None and pincode !='':
            account.pincode = pincode
        account.save()

        return  redirect('/account/')

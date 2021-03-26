from django.contrib import admin
from .models import New_sup,S_prod,Products,Notify,Bank_verify,Entity_verify,Representative_verify

# Register your models here.
admin.site.register(New_sup)
admin.site.register(S_prod)
admin.site.register(Products)
admin.site.register(Notify)
admin.site.register(Bank_verify)
admin.site.register(Entity_verify)
admin.site.register(Representative_verify)
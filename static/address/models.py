from account.models import Account
from django.core.validators import RegexValidator
from django.db import models


class Address(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,blank=False,null=False)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    regexp = RegexValidator(regex=r'^\d{6}$',message="Invalid Pin Code Number")
    pincode = models.CharField(validators=[regexp], max_length=6)
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    isAddressVerified = models.BooleanField(default=False)
    ADDRESS_CHOICES=[
        ('COMPANY','COMPANY'),
        ('Representative','REPRESENTATIVE')
    ]
    addressType = models.CharField(max_length=20,choices=ADDRESS_CHOICES)
    def __str__(self):
        return self.address

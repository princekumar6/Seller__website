from account.models import Account
from django.core.validators import RegexValidator
from django.db import models


class Address(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,blank=False,null=False)
    city = models.CharField(max_length=100)
    STATE_CHOICES=[
        ("AP","Andhra Pradesh"),
        ("AR","Arunachal Pradesh"),
        ("AS","Assam"),
        ("BR","Bihar"),
        ("CG","Chhattisgarh"),
        ("Chandigarh","Chandigarh"),
        ("DN","Dadra and Nagar Haveli"),
        ("DD","Daman and Diu"),
        ("DL","Delhi"),
        ("GA","Goa"),
        ("GJ","Gujarat"),
        ("HR","Haryana"),
        ("HP","Himachal Pradesh"),
        ("JK","Jammu and Kashmir"),
        ("JH","Jharkhand"),
        ("KA","Karnataka"),
        ("KL","Kerala"),
        ("MP","Madhya Pradesh"),
        ("MH","Maharashtra"),
        ("MN","Manipur"),
        ("ML","Meghalaya"),
        ("MZ","Mizoram"),
        ("NL","Nagaland"),
        ("OR","Orissa"),
        ("PB","Punjab"),
        ("PY","Pondicherry"),
        ("RJ","Rajasthan"),
        ("SK","Sikkim"),
        ("TN","Tamil Nadu"),
        ("TR","Tripura"),
        ("UP","Uttar Pradesh"),
        ("UK","Uttarakhand"),
        ("WB","West Bengal")
    ]
    state = models.CharField(max_length=50)
    regexp = RegexValidator(regex=r'^\d{6}$',message="Invalid Pin Code Number")
    pincode = models.CharField(validators=[regexp], max_length=6)
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    isAddressVerified = models.BooleanField(default=False)
    ADDRESS_CHOICES=[
        ('COMPANY','Company'),
        ('REPRESENTATIVE','Representative'),
        ('OTHER','Other')
    ]
    addressType = models.CharField(max_length=20,choices=ADDRESS_CHOICES)
    def __str__(self):
        return self.address

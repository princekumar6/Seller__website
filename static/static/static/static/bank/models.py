from datetime import datetime

from account.models import Account
from django.db import models


class Bank(models.Model):
    STATUS_CHOICES=[
        ('YES','Yes'),
        ('NO','No'),
        ('Invalid','Invalid')
    ]
    account = models.ForeignKey(Account,on_delete=models.SET_NULL, null=True,blank=True)
    accountHolderName = models.CharField(max_length=30)
    accontNumber = models.CharField(max_length=30,unique=True)
    ifsc = models.CharField(max_length=30)
    bank = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='NO')
    date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.accountHolderName

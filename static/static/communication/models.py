from account.models import Account
from django.db import models


class Notification(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    isReaded = models.BooleanField(default=False)
    def __str__(self):
        return self.message


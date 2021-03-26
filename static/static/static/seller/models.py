from django.db import models
from django.utils import timezone

# Create your models here.
class New_sup(models.Model):
    sup_id = models.CharField(max_length=100,unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    numb = models.CharField(max_length=13,unique=True)
    pswd = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=50)
    company = models.CharField(max_length=200,blank=True,null=True)
    c_represent = models.CharField(max_length=100,blank=True,null=True)
    categories = models.CharField(max_length=1000,blank=True,null=True)
    pickup = models.CharField(max_length=1000,blank=True,null=True)
    verified = models.CharField(default='No',max_length=4)
    id_verified = models.CharField(default='No',max_length=4)
    email_verified = models.CharField(default='No',max_length=4)
    bank_verified = models.CharField(default='No',max_length=4)
    comm = models.IntegerField(default=5)
    clogo = models.ImageField(upload_to='media/')
    account_status = models.CharField(default='Active',max_length=10)
    about = models.CharField(max_length=1000,blank=True,null=True)
    verifyby = models.CharField(max_length=100,blank=True,null=True)
    gst = models.CharField(max_length=30)

    def __str__(self):
        return self.sup_id

class Bank_verify(models.Model):
    sup_id = models.ForeignKey(New_sup,on_delete=models.DO_NOTHING)
    account_name = models.CharField(max_length=30)
    account_number = models.CharField(max_length=30,unique=True)
    ifsc = models.CharField(max_length=30)
    bank = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    status = models.CharField(max_length=5,default='No')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.account_number

class Entity_verify(models.Model):
    sup_id = models.ForeignKey(New_sup,on_delete=models.DO_NOTHING)
    bank_pan = models.CharField(max_length=30,unique=True)
    e_kyc = models.CharField(max_length=20)
    status = models.CharField(max_length=30,default='No')
    e_doc = models.FileField(upload_to='media/')
    corporate = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bank_pan

class Representative_verify(models.Model):
    sup_id = models.ForeignKey(New_sup,on_delete=models.DO_NOTHING)
    sup_name = models.CharField(max_length=50,unique=True)
    r_name = models.CharField(max_length=30)
    r_dob = models.IntegerField(default=0)
    r_address = models.CharField(max_length=30)
    r_kyc = models.CharField(max_length=30)
    status = models.CharField(max_length=30,default='No')
    r_doc = models.FileField(upload_to='media/')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sup_name

class S_prod(models.Model):
    sup_id = models.ForeignKey(New_sup,on_delete=models.DO_NOTHING)
    prod_id = models.CharField(primary_key=True,max_length=50)
    desc = models.CharField(max_length=1000,blank=True,null=True)
    heading = models.CharField(max_length=200,blank=True,null=True)
    prod_img = models.CharField(max_length=10000,blank=True,null=True)
    frstimg = models.CharField(max_length=1000,blank=True,null=True)
    sub_c = models.CharField(max_length=100,blank=True,null=True)
    category = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    hsn = models.CharField(max_length=100,blank=True,null=True)
    warranty = models.CharField(max_length=100,blank=True,null=True)
    guarantee = models.CharField(max_length=100,blank=True,null=True)
    inventory = models.IntegerField(default=0)
    prod_l = models.CharField(max_length=100,blank=True,null=True)
    prod_w = models.CharField(max_length=100,blank=True,null=True)
    prod_h = models.CharField(max_length=100,blank=True,null=True)
    box_l = models.IntegerField(default=0)
    box_w = models.IntegerField(default=0)
    box_h = models.IntegerField(default=0)
    s_weight = models.FloatField(default=0)
    colour = models.CharField(max_length=100,default='')
    size = models.CharField(max_length=100,default='')
    material = models.CharField(max_length=100,blank=True,null=True)
    marked = models.CharField(max_length=100,blank=True,null=True)
    listed = models.CharField(max_length=100,blank=True,null=True)
    sale = models.FloatField(default=0)
    disbursement = models.FloatField(default=0)
    prod_status = models.CharField(default='Active',max_length=10)
    about = models.CharField(default='',max_length=1000)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.prod_id

class Notify(models.Model):
    sup_id = models.ForeignKey(New_sup,on_delete=models.DO_NOTHING)
    notifications = models.CharField(primary_key=True,max_length=15)
    n1 = models.CharField(max_length=100,blank=True,null=True)
    s1 = models.IntegerField(default=800)
    l1 = models.CharField(max_length=100,blank=True,null=True)
    n2 = models.CharField(max_length=100,blank=True,null=True)
    s2 = models.IntegerField(default=800)
    l2 = models.CharField(max_length=100,blank=True,null=True)
    n3 = models.CharField(max_length=100,blank=True,null=True)
    s3 = models.IntegerField(default=800)
    l3 = models.CharField(max_length=100,blank=True,null=True)
    coun = models.IntegerField(default=3)

    def __str__(self):
        return self.notifications

class Products(models.Model):
    na = models.CharField(max_length=10,primary_key=True)
    product = models.IntegerField(default=1)
    number = models.IntegerField(default=1)
    productimg = models.IntegerField(default=1)
    discussid = models.IntegerField(default=1)

    def __str__(self):
        return self.na

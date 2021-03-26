import os.path
from os.path import join
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from django.core.validators import RegexValidator
from django.db import models
from theseventhsquare.settings import BASE_DIR

KYCDocStorage = FileSystemStorage(location=os.path.join(BASE_DIR,'KYCDoc'))

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid4(), ext)
    return join('account/', filename)

def get_file_path_company(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid4(), ext)
    return join('company/', filename)

def get_file_path_company_doc(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid4(), ext)
    return join('companyKYCdoc/', filename)

def get_file_path_company_repr_doc(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid4(), ext)
    return join('RepresentativeKYCdoc/', filename)

class Account(AbstractUser):
    #account Related Field
    Representativename = models.CharField(max_length=20, blank=True, null=True)
    Representativeimage = models.ImageField(upload_to=get_file_path,verbose_name='image',blank=True)

    REPR_CHOICES=[
        ('Aadhar','Aadhar'),
        ('PAN',"PAN"),
        ('Passport','Passport')
    ]
    RepresentativeDocType = models.CharField(max_length=10,choices=REPR_CHOICES,null=True,blank=True)
    RepresentativeDoc = models.FileField(storage=KYCDocStorage,upload_to=get_file_path_company_repr_doc,null=True,blank=True)
    RepresentativeDOB = models.DateField(null=True,blank=True)
    # Mobile related Field
    mobilenovalidation = RegexValidator(regex=r'^[6-9]\d{9}$', message="Invalid mobile number")
    mobileNumber = models.TextField(validators=[mobilenovalidation], max_length=13, blank=False,unique=True)
    mobileVerificationCode = models.CharField(max_length=10,blank=True)
    isMobileNumberVerified = models.BooleanField(default=False)
    # Email related Field
    email = models.EmailField(null=True,blank=True,unique=True)
    emailVerificationCode = models.CharField(max_length=10,blank=True)
    isEmailVerified = models.BooleanField(default=False)

    #company related field    
    companyName = models.CharField(max_length=250,blank=False,null=False)
    companyImage = models.ImageField(upload_to=get_file_path_company,verbose_name='image',blank=True)
    companyAbout = models.CharField(max_length=500,blank=True,null=True)

    COMAPNY_CATEGORY=[
        ('Interior Items','Interior Items'),
        ('Construction','Construction')
    ]
    companyCategory = models.CharField(max_length=20,choices=COMAPNY_CATEGORY,null=True,blank=True)


    DOC_TYPE_CHOIES=[
        ('Certificate Of Incorporation','Certificate Of Incorporation'),
        ('GST Registration Certificate','GST Registration Certificate'),
        ('IT Return','IT Return'),
        ('Registration Certificate','Registration Certificate')
    ]
    companyGSTNumber = models.CharField(max_length=30)
    companyPAN = models.CharField(max_length=10,null=True,blank=True)
    companyCIN = models.CharField(max_length=30,null=True,blank=True)
    companyKYCDocType = models.CharField(max_length=30,choices=DOC_TYPE_CHOIES,null=True,blank=True)
    companyKYCDOC = models.FileField(upload_to=get_file_path_company_doc,storage=KYCDocStorage,null=True,blank=True)

    # notification regards
    #notificationCount = models.PositiveIntegerField(default=0)

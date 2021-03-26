from os.path import join
from uuid import uuid4

from django.db import models


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid4(), ext)
    return join('product/', filename)
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200,null=True)
    parent = models.ForeignKey('self',null=True,on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path,verbose_name='image',null=False,blank=False)
    description = models.CharField(max_length=200, null=True)
    
class Variant (models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

class Keyvalue(models.Model):
    variant=models.ForeignKey(Variant,on_delete=models.CASCADE)
    key=models.CharField(max_length=100)
    value=models.CharField(max_length=100)

class Attribute(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    value=models.CharField(max_length=200,null=False,blank=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
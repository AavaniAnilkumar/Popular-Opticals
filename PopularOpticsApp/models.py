from django.db import models

# Create your models here.

class staffdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    desi = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="profile",null=True,blank=True)

class catdb(models.Model):
    catname = models.CharField(max_length = 100, null=True,blank=True)
    desc =  models.CharField(max_length = 100, null=True,blank=True)
    image = models.ImageField(upload_to="profiles",null=True,blank=True)

class prodb(models.Model):
    category = models.CharField(max_length=100,null=True,blank=True)
    productname = models.CharField(max_length=100,null=True,blank=True)
    desc = models.CharField(max_length=100,null=True,blank=True)
    frame = models.CharField(max_length=100,null=True,blank=True)
    size = models.CharField(max_length=100,null=True,blank=True)
    rate = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to="profiles",null=True,blank=True)


class contactdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.CharField(max_length=500,null=True,blank=True)

class estimatedb(models.Model):
    country = models.CharField(max_length=150,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    zip = models.IntegerField(null=True,blank=True)



from django.db import models
from phonenumber_field.modelfields import  PhoneNumberField

# Create your models here.




class Distributor(models.Model):
    service_ch =[('credit','credit'),('games','games')]
    name = models.CharField(max_length=200,null=True,blank=False)
    phone = PhoneNumberField(null=True,blank=False)
    address = models.CharField(max_length=200,null=True,blank=False)
    facebook = models.CharField(max_length=200,null=True,blank=False)
    service = models.CharField(choices=service_ch,max_length=20,null=True,blank=False)
    ccp = models.BigIntegerField(null=True,blank=False)
    key = models.IntegerField(null=True,blank=False)
    def __str__(self):
        return self.name

class ServiceCredit(models.Model):
    currency_ch = [('€','€'),('$','$'),('DZD','DZD')]
    distributor = models.ForeignKey(Distributor,on_delete=models.SET_NULL,null=True,blank=False)
    name = models.CharField(max_length=200,null=True,blank=False)
    price = models.FloatField(default=0.00)
    currency = models.CharField(choices=currency_ch,max_length=20,null=True,blank=False)
    available = models.FloatField(null=True,blank=False)
    image = models.ImageField(default='defser.png')
    def __str__(self):
        return self.name

class ServiceGame(models.Model):
    currency_ch = [('€','€'),('$','$'),('DZD','DZD'),('Unit','Unit')]
    distributor = models.ForeignKey(Distributor,on_delete=models.SET_NULL,null=True,blank=False)
    name = models.CharField(max_length=200,null=True,blank=False)
    price = models.FloatField(default=0.00)
    currency = models.CharField(choices=currency_ch,max_length=20,null=True,blank=False)
    available = models.FloatField(null=True,blank=False)
    image = models.ImageField(default='defser.png')
    def __str__(self):
        return self.name
        
class Order(models.Model):
    saller = models.CharField(blank=True,max_length=200)
    name = models.CharField(max_length=200,null=True,blank=False)
    phone = models.FloatField(null=True,blank=False)
    amount = models.FloatField(null=True,blank=False)
    email = models.EmailField(null=True,blank=True)
    accountId = models.TextField(default='',blank=False)
    image = models.ImageField('Label')

    def __str__(self):
        return self.saller


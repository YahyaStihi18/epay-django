from django.db import models
from phonenumber_field.modelfields import  PhoneNumberField
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.




class Distributor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    service_ch =[('credit','credit'),('games','games')]
    phone = PhoneNumberField(null=True,blank=False)
    address = models.CharField(max_length=200,null=True,blank=False)
    facebook = models.CharField(max_length=200,null=True,blank=False)
    ccp = models.BigIntegerField(null=True,blank=False)
    key = models.IntegerField(null=True,blank=False)
    rip = models.BigIntegerField(null=True,blank=False)

    def __str__(self):
        return self.user.username


class Service(models.Model):
    type_ch = [('credit','credit'),('game','game'),('other','other')]
    currency_ch = [('€','€'),('$','$'),('DZD','DZD'),('Unit','Unit')]
    distributor = models.ForeignKey(Distributor,on_delete=models.SET_NULL,null=True,blank=False)
    model = models.CharField(choices=type_ch,max_length=20,null=True,blank=False)
    name = models.CharField(max_length=200,null=True,blank=False)
    price = models.FloatField(default=0.00)
    currency = models.CharField(choices=currency_ch,max_length=20,null=True,blank=False)
    available = models.FloatField(null=True,blank=False)
    note = models.TextField(null=True,blank=True)
    image = models.ImageField(default='defser.png')
    def __str__(self):
        return self.name
        
class Order(models.Model):
    status_ch = [('in process','in process'),('complete','complete')]
    visible_ch = [('yes','yes'),('no','no')]
    status = models.CharField(choices=status_ch,max_length=20,null=True,blank=False,default='in process')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    distributor = models.CharField(blank=True,max_length=200)
    product = models.CharField(blank=True,max_length=200)
    currency = models.CharField(blank=True,max_length=200)
    name = models.CharField(max_length=200,null=True,blank=False)
    phone = models.IntegerField(null=True,blank=False)
    amount = models.FloatField(null=True,blank=False)
    email = models.EmailField(null=True,blank=True)
    accountId = models.TextField(default='',blank=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('Label')
    visible_for_distributor = models.BooleanField(default=True)
    visible_for_buyer = models.BooleanField(default=True)

    def __str__(self):
        return self.distributor

class Email(models.Model):
    name = models.CharField(max_length=200,null=True,blank=False)
    email = models.EmailField(null=True,blank=False)
    text = models.TextField(default='',blank=False)
    time = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    




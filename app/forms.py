from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = ['name','phone','amount','email','image','accountId']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['accountId'].widget.attrs['class'] = 'form-control-account'


class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['distributor','model','name','price','currency','available','note','image']
        
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['model'].widget.attrs['class'] = 'form-control-account'
        self.fields['name'].widget.attrs['class'] = 'form-control-account'
        self.fields['distributor'].widget.attrs['class'] = 'form-control-account'
        self.fields['price'].widget.attrs['class'] = 'form-control-account'
        self.fields['currency'].widget.attrs['class'] = 'form-control-account'
        self.fields['available'].widget.attrs['class'] = 'form-control-account'
        self.fields['note'].widget.attrs['class'] = 'form-control-account'


        


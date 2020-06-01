from django import forms
from .models import *

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

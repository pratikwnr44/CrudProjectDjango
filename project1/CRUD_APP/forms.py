from django import forms
from .models import Order

class OrdeerForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'd_Date': forms.DateInput(attrs={
                'type':'date'
            }),
            'add': forms.Textarea(attrs={
                'placeholder':'karve nagar'
            })
        }

        labels = {
            'o_id':'ORDER ID',
            'name':'CUSTOMER NAME',
            'product':'PRODUCT NAME',
            'd_Date':'DILEVERY DATE',
            'add':'ADDRESS',
            'price':'PRICE'

        }
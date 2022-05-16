from django import forms
from django.forms import ModelForm
from .models import Item

class ItemCreate(ModelForm):
    class Meta:
        model = Item
        
        fields = ('name', 'description', 'price', 'quantity')

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'Description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'Price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'Quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        }
"""
class ItemDelete(ModelForm):
    class Meta:
        model = Item
        
        fields = ('deletion_comments',)

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'Description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'Price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'Quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        }
"""
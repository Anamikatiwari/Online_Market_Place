from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    c

fields = ('category', 'name', 'description', 'price', 'image')
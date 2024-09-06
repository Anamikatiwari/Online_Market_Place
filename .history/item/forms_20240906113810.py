from django import forms

from .models import Item

class NewItemForm(forms.ModelForm)

fields = ('category', 'name', 'description', 'price', 'image')
from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta

fields = ('category', 'name', 'description', 'price', 'image')
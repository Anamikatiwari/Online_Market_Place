from django.shortcuts import render

from item.models import Category, Item

# Create your views here.

def index(request):
    items = Item.objects.filter
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')
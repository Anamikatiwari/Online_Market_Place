from django.shortcuts import render, get_object_or_404

from.o

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item
# Create your views here.


@login_required
def index(request)

from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('new', views.conversation, name='conversation'),
]

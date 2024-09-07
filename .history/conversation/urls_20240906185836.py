
from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('new/<item', views.conversation, name='conversation'),
]

from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('new/', v)
    path('<int:pk>/', views.detail, name='detail'),
]

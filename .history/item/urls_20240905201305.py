from django.urls import path
from . import views

app

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]

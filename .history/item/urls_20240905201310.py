from django.urls import path
from . import views

app_name = ''

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]

from django.urls import path
from . import views

app_name = 'alert'

urlpatterns = [
    path('alert', views.alert, name='alert'),
]

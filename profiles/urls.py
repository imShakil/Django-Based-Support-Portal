from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('open-tickets', views.tickets, name='open-ticket'),
    path('profile', views.profile, name='profile'),
]

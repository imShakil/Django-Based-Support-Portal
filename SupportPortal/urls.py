"""SupportPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from profiles import views as profileViews
from alerts import views as alertViews
from tickets import views as ticketViews


urlpatterns = [
    path("", views.dashboard, name='home'),
    path("admin/", admin.site.urls),
    path("ticket/", include("tickets.urls")),
    path("dashboard/", include("profiles.urls")),
    path("search/", include("search.urls")),
    path("alert/", include("alerts.urls")),
    path("facultynstaff/<int:id>", views.facultynstaff, name='faculty and staff')
]


import django.urls 
from django.urls import include
from . import views

urlpatterns = [
    django.urls.path('', views.home, name='home'),
    django.urls.path("accounts/", include("allauth.urls")),
]
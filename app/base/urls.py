from django.urls import path

from app.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
]

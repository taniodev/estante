from django.urls import path

from app.books import views

app_name = 'books'

urlpatterns = [
    path('', views.reading_now, name='reading_now'),
]

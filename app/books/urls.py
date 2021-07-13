from django.urls import path

from app.books import views

app_name = 'books'

urlpatterns = [
    path('', views.reading_now, name='reading_now'),
    path('add', views.add_book, name='add_book'),
]

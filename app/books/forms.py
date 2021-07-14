from django.forms import ModelForm

from app.books.models import BookModel


class BookForm(ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'author', 'published', 'description', 'read_status']

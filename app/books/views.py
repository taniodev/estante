from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.books.forms import BookForm


@login_required
def reading_now(request):
    return render(request, 'books/reading_now.html')


@login_required
def add_book(request):
    form = BookForm()

    return render(request, 'books/add_book.html', {
        'form': form,
    })

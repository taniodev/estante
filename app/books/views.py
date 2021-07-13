from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def reading_now(request):
    return render(request, 'books/reading_now.html')


@login_required
def add_book(request):
    return render(request, 'books/add_book.html')

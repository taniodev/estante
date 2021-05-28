from django.shortcuts import render


def reading_now(request):
    return render(request, 'books/reading_now.html')

from django.shortcuts import render, HttpResponse
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()
    # return HttpResponse("Books app")
    return render(request, 'books/index.template.html', {
        'books': books
    })

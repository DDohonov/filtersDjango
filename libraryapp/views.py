from django.shortcuts import render
from .models import *


def show_books(request):
    if request.method == 'POST':
        if 'book_name' in request.POST:
            book_name = request.POST['book_name']
            list_books = Book.objects.filter(name__icontains=book_name)
            context = {
                'list_books': list_books,
                'selection_criterion': f'Усі збіги за іменем книжки "{book_name}"'
            }
        elif 'author_name' in request.POST:
            author_name = request.POST['author_name']
            list_authors = Author.objects.filter(name__icontains=author_name)
            list_books = []
            for author in list_authors:
                list_books += Book.objects.filter(author_id = author.id)
            context = {
                'list_books': list_books,
                'selection_criterion': f'Усі збіги за іменем автора "{author_name}"'
            }
    else:
        context = {
            'list_books': Book.objects.all(),
            'selection_criterion': 'Усі книжки'
        }

    return render(request, 'books.html', context=context)


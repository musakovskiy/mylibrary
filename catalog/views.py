from django.http import HttpRequest, HttpResponse
from .models import Book, Author, LiteraryFormat
from django.shortcuts import render
from django.views import generic


def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_literary_formats = LiteraryFormat.objects.count()
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_literary_formats": num_literary_formats
    }
    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(generic.ListView):
    model = LiteraryFormat
    template_name = 'catalog/literary_format_list.html'
    context_object_name = 'literary_format_list'


# def literary_format_list_view(request: HttpRequest) -> HttpResponse:
# literary_format_list = LiteraryFormat.objects.all()
# context = {
# "literary_format_list": literary_format_list
# }
# return render(request, "catalog/literary_format_list.html", context=context)


class BookListView(generic.ListView):
    model = Book

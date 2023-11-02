from django.http import HttpRequest, HttpResponse
from .models import Book, Author, LiteraryFormat
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_literary_formats = LiteraryFormat.objects.count()
    num_vizits = request.session.get("num_vizits", 0)
    request.session["num_vizits"] = num_vizits + 1
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_literary_formats": num_literary_formats,
        "num_vizits": num_vizits + 1
    }
    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(generic.ListView):
    model = LiteraryFormat
    template_name = 'catalog/literary_format_list.html'
    context_object_name = 'literary_format_list'


class LiteraryFormatCreateView(generic.CreateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatUpdateView(generic.UpdateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary_format_form.html"


class BookListView(generic.ListView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


def book_detail_view(request, pk: int) -> HttpResponse:
    book = Book.objects.get(id=pk)
    context = {
        'book': book
    }
    return render(request, "catalog/book_detail.html", context=context)


def test_session_view(request: HttpRequest) -> HttpResponse:
    request.session["book"] = "test session book"
    request.session["format"] = "test format"
    num_vizit = request.session.get("new", 0)
    request.session["new"] = num_vizit + 1
    return HttpResponse(
        "<h1>Test Session</h1>"
        f"<h4>Session Data: {request.session['book']}</4>"
        f"<h3>New Session Data: {request.session['format']}"
        f" <h4>You vizit this site : {num_vizit} times </h4>"
    )

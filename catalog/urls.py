from django.urls import path

from catalog.views import (index,
                           LiteraryFormatListView,
                           BookListView,
                           AuthorListView,
                           book_detail_view,
                           LiteraryFormatCreateView,
                           LiteraryFormatUpdateView,
                           )

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("literary-formats/create", LiteraryFormatCreateView.as_view(), name="literary-format-create"),
    path("literary-formats/<int:pk>/update", LiteraryFormatUpdateView.as_view(), name="literary-format-update"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("books/<int:pk>/", book_detail_view, name="book-detail"),
]
app_name = "catalog"

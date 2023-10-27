from django.urls import path

from catalog.views import index, LiteraryFormatListView, BookListView

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("books/", BookListView.as_view(), name="book-list")
]
app_name = "catalog"

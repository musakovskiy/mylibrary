from django.urls import path

from catalog.views import index, LiteraryFormatListView, BookListView, AuthorListView, book_detail_view, test_session_view

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("books/<int:pk>/", book_detail_view, name="book-detail"),
    path('test-session/', test_session_view, name="test-session")
]
app_name = "catalog"

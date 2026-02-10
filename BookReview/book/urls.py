from django.urls import path
from . import views

urlpatterns = [
    path("book/new", views.BookCreateView.as_view(), name="Book_create"),
    path("", views.BookListView.as_view(), name="booklist"),
    path("book/<int:pk>/", views.BookDetailView(), name="bookdetail"),
    path("book/<int:pk>/edit/", views.BookUpdateView.as_view(), name="bookupdate"),
    path("book/<int:pk>/delete/", views.BookDeleteView.as_view(), name="bookdelete"),
]

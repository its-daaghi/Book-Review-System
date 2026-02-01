from django.urls import path
from . import views

urlpatterns = [
    path("book/new", views.Book_create, name="Book_create"),
    path("", views.booklist, name="booklist"),
    path("book/<int:pk>/", views.bookdetail, name="bookdetail"),
    path("book/<int:pk>/edit/", views.book_update, name="bookupdate"),
    path("book/<int:pk>/delete/", views.book_delete, name="bookdelete"),
]

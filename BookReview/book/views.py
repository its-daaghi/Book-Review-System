from django.shortcuts import render, redirect
from book.forms import bookForm
from django.contrib import messages
from .models import Book


# Create your views here.
def Book_create(request):
    if request.method == "POST":
        form = bookForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Book Created Succesfully!")
            return redirect("Book_create")
    else:
        form = bookForm()

    return render(request, "book/book_form.html", {"form": form})


def booklist(request):

    books = Book.objects.all().order_by("created_at")
    return render(request, "book/book_list.html", {"books": books})


def bookdetail(request, pk):
    book = Book.objects.get(pk=pk)

    return render(request, "book/book_detail.html", {"book": book})


def book_update(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == "POST":
        form = bookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            messages.success(request, "Book updated Succesfully!")
            return redirect("bookupdate", pk=book.pk)
    else:
        form = bookForm(instance=book)
    return render(request, "book/book_form.html", {"form": form})


def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("booklist")

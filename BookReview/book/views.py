from django.views.generic import TemplateView, RedirectView
from django.shortcuts import render, redirect
from book.forms import bookForm
from django.contrib import messages
from .models import Book
from django.views import View


# Create your views here.
class BookCreateView(View):
    def get(self, request):
        form = bookForm()
        return render(request, "book/book_form.html", {"form": form})

    def post(self, request):
        form = bookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully")
            redirect("booklist")
        return render(request, "book/book_form.html", {"form": form})


# def Book_create(request):
#     if request.method == "POST":
#         form = bookForm(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(request, "Book Created Succesfully!")
#             return redirect("Book_create")
#     else:
#         form = bookForm()

#     return render(request, "book/book_form.html", {"form": form})


class BookListView(TemplateView):
    template_name = "book/book_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = self.request.GET.get("genre")
        if genre:
            context["books"] = Book.objects.filter(genre=genre).order_by("-created_at")
        else:
            context["books"] = Book.objects.all().order_by("-created_at")
        return context


# def booklist(request):

#     books = Book.objects.all().order_by("created_at")
#     return render(request, "book/book_list.html", {"books": books})


class BookDetailView(TemplateView):
    template_name = "book/book_detail.html "

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get("pk")
        context["book"] = Book.objects.get(pk=pk)
        return context


# def bookdetail(request, pk):
#     book = Book.objects.get(pk=pk)

#     return render(request, "book/book_detail.html", {"book": book})


class BookUpdateView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        form = bookForm(instance=book)
        return render(request, "book/book_form.html", {"form": form})

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        form = bookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book Updated successfully")
            redirect("booklist")
        return render(request, "book/book_form.html", {"form": form})


# def book_update(request, pk):
#     book = Book.objects.get(pk=pk)

#     if request.method == "POST":
#         form = bookForm(request.POST, instance=book)

#         if form.is_valid():
#             form.save()
#             messages.success(request, "Book updated Succesfully!")
#             return redirect("bookupdate", pk=book.pk)
#     else:
#         form = bookForm(instance=book)
#     return render(request, "book/book_form.html", {"form": form})


class BookDeleteView(RedirectView):
    pattern_name = "booklist"

    def get_redirect_url(self, *args, **kwargs):
        pk = kwargs.get("pk")
        book = Book.objects.get(pk=pk)
        book.delete()
        messages.success(self.request, "Book Deleted Successfully")
        return super().get_redirect_url()


# def book_delete(request, pk):
#     book = Book.objects.get(pk=pk)
#     book.delete()
#     return redirect("booklist")

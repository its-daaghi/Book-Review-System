from django import forms
from .models import Book


class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "genre", "isbn", "publication_date"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title of book"}
            ),
            "author": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter name of author"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "4",
                    "placeholder": "Enter Description about book",
                }
            ),
            "genre": forms.Select(attrs={"class": "form-control"}),
            "isbn": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Isbn"}
            ),
            "publication_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }

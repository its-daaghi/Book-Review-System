from django.db import models


# Create your models here.
class Book(models.Model):
    Genre_Choices = [
        ("fiction", "Fiction"),
        ("nonfiction", "NoNFiction"),
        ("science", "Science"),
        ("english", "English"),
        ("history", "History"),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=200, choices=Genre_Choices)
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    publication_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

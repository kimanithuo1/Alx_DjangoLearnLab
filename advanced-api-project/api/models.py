from django.db import models

class Author(models.Model):
    """
    Represents a book author.
    Each author can have multiple books linked through the Book model.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book with a title, publication year, and a link to its author.
    Establishes a One-to-Many relationship with Author (many books per author).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

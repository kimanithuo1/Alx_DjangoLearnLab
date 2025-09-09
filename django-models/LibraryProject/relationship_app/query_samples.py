from .models import Author, Book, Library

def queries():
    # 1. All books by a specific author
    author = Author.objects.get(name="Ngugi wa Thiong'o")
    books_by_author = Book.objects.filter(author=author)

    # 2. All books in a library
    library = Library.objects.get(name="library_name")
    books_in_library = library.books.all()

    # 3. Librarian of a library
    librarian = library.librarian  

    return books_by_author, books_in_library, librarian
# Note: The above code assumes that the database has been populated with relevant data.
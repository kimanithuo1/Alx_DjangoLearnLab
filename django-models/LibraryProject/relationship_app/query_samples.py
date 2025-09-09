from .models import Author, Book, Library

def queries():
    # 1. Query all books by a specific author
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)

    # 2. List all books in a library
    library_name = "LibraryProject"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()

    # 3. Retrieve the librarian for a library
    librarian = library.librarian

    return books_by_author, books_in_library, librarian
# Note: The above code assumes that the database has been populated with relevant data.
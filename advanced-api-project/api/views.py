from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ---------------------------
# LIST ALL BOOKS
# ---------------------------
class BookListView(generics.ListAPIView):
    """
    GET: Retrieve all books (open to all users)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ---------------------------
# CREATE NEW BOOK
# ---------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# RETRIEVE BOOK BY ID
# ---------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve book by ID (open to all users)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ---------------------------
# UPDATE BOOK
# ---------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update a book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# DELETE BOOK
# ---------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


"""
API Views for Book model:
- BookListCreateView: Handles listing all books and creating new ones.
- BookDetailView: Handles retrieving, updating, and deleting a book by ID.

Permissions:
- Read operations (GET) are open to all users.
- Write operations (POST, PUT, PATCH, DELETE) require authentication.
"""

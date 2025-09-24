from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# List all books / Create a new book
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: Retrieve all books
    POST: Create a new book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow unauthenticated users to view, but restrict creation
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Retrieve a single book / Update / Delete
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve book by ID
    PUT/PATCH: Update book (requires authentication)
    DELETE: Delete book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow unauthenticated users to read, but restrict modification
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

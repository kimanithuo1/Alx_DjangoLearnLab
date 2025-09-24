from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer


# ---------------------------
# LIST ALL BOOKS
# ---------------------------
class BookListView(generics.ListAPIView):
    """
    GET: Retrieve all books (with filtering, searching, ordering)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    # Filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields available for filtering
    filterset_fields = ['title', 'publication_year', 'author']

    # Fields available for search
    search_fields = ['title', 'author__name']

    # Fields available for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# ---------------------------
# CREATE NEW BOOK
# ---------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ---------------------------
# RETRIEVE BOOK BY ID
# ---------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve book by ID (open to all users)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# ---------------------------
# UPDATE BOOK
# ---------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update a book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ---------------------------
# DELETE BOOK
# ---------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

"""
API Views for Book model:
- BookListCreateView: Handles listing all books and creating new ones.
- BookDetailView: Handles retrieving, updating, and deleting a book by ID.

Permissions:
- Read operations (GET) are open to all users.
- Write operations (POST, PUT, PATCH, DELETE) require authentication.
"""



"""
Enhancements in BookListCreateView:
- filterset_fields: Allows filtering by title, publication_year, and author.
- search_fields: Enables searching across book titles and author names.
- ordering_fields: Supports ordering results by title or publication_year.
"""

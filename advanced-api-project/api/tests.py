from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create some sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2001)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2005)

        # Authenticate client for write operations
        self.client.login(username="testuser", password="password123")

    # ---------------------------
    # LIST BOOKS
    # ---------------------------
    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    # ---------------------------
    # CREATE BOOK
    # ---------------------------
    def test_create_book_authenticated(self):
        url = reverse("book-create")
        data = {"title": "New Book", "author": "Author C", "publication_year": 2010}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        url = reverse("book-create")
        data = {"title": "Unauthorized Book", "author": "Author X", "publication_year": 2020}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------------------------
    # RETRIEVE BOOK
    # ---------------------------
    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

    # ---------------------------
    # UPDATE BOOK
    # ---------------------------
    def test_update_book_authenticated(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Book One", "author": "Author A", "publication_year": 2001}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_update_book_unauthenticated(self):
        self.client.logout()
        url = reverse("book-update", args=[self.book2.id])
        data = {"title": "Should Not Update", "author": "Author B", "publication_year": 2005}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------------------------
    # DELETE BOOK
    # ---------------------------
    def test_delete_book_authenticated(self):
        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        self.client.logout()
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------------------------
    # FILTER / SEARCH / ORDER
    # ---------------------------
    def test_filter_books_by_author(self):
        url = reverse("book-list") + "?author=Author A"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author A")

    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=Book Two"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book Two")

    def test_order_books_by_year(self):
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data[0]["publication_year"], response.data[1]["publication_year"])

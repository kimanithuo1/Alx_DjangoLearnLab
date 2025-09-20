from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

#create a router and register our viewsets with it.

router= DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')



urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]

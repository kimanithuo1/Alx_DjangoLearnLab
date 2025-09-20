from django.contrib import admin
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


#create a router and register our viewsets with it.

router= DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),  # Endpoint for obtaining auth token
]

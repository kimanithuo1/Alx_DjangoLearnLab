from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
from .views import registerView, loginView, logoutView


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path('register_view/', registerView.as_view(), name='register_view'),
    path('login_view/', loginView.as_view(), name='login_view'),
    path('logout_view/', logoutView.as_view(), name='logout_view'),
    
]
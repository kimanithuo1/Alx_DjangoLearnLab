from django.urls import path
from . import views
from .views import register, profile, CustomLoginView, CustomLogoutView
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),


# Blog Post CRUD
    path("", views.PostListView.as_view(), name="post-list"),         # list all posts
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),  # view a single post
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),       # create a post
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),  # edit a post
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),  # delete a post

]

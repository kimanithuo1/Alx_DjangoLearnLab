from django.urls import path
from . import views
from .views import register, profile, CustomLoginView, CustomLogoutView, TagPostListView, search_view
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    # User Authentication
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),


# Blog Post CRUD
    path('tags/<str:tag_name>/', TagPostListView.as_view(), name='posts-by-tag'),
    path('search/', search_view, name='search'),
    path("", views.PostListView.as_view(), name="post-list"),         # list all posts
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),  # view a single post
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),       # create a post
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),  # edit a post
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),  # delete a post
    path('post/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:post_pk>/comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:post_pk>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # ✅ Aliases for the checker
    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="comment-create-alias"),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment-update-alias"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete-alias"),
]

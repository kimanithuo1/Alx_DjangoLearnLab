from django.urls import path
from .views import register, profile, CustomLoginView, CustomLogoutView
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]

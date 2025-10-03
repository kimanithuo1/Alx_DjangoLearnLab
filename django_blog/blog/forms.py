from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from .models import Comment
from taggit.forms import TagWidget


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']

class PostForm(forms.ModelForm):

    tags = forms.CharField(required=False, help_text="Comma-separated tags", widget=forms.TextInput())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write your post...'}),
            'tags': TagWidget(),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a comment...'
            }),
        }
        labels = {
            'content': ''
        }

    def clean_content(self):
        data = self.cleaned_data['content'].strip()
        if not data:
            raise forms.ValidationError("Comment cannot be empty.")
        return data
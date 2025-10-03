from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment

class AuthTests(TestCase):
    def test_register_view(self):
        resp = self.client.get(reverse('blog:register'))
        self.assertEqual(resp.status_code, 200)

    def test_user_registration(self):
        data = {
            'username': 'tester1',
            'email': 'tester@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
        }
        resp = self.client.post(reverse('blog:register'), data, follow=True)
        self.assertTrue(User.objects.filter(username='tester1').exists())
        self.assertEqual(resp.status_code, 200)

class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass12345')
        self.other = User.objects.create_user(username='other', password='pass12345')
        self.post = Post.objects.create(title='Test post', content='Content', author=self.user)

    def test_post_list_view(self):
        resp = self.client.get(reverse('blog:post-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test post')

    def test_create_requires_login(self):
        resp = self.client.get(reverse('blog:post-create'))
        self.assertNotEqual(resp.status_code, 200)  # redirect to login

        self.client.login(username='author', password='pass12345')
        resp = self.client.get(reverse('blog:post-create'))
        self.assertEqual(resp.status_code, 200)

    def test_only_author_can_edit(self):
        self.client.login(username='other', password='pass12345')
        resp = self.client.get(reverse('blog:post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 403)  # UserPassesTestMixin returns 403 if test fails

        self.client.login(username='author', password='pass12345')
        resp = self.client.get(reverse('blog:post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_delete_post(self):
        self.client.login(username='author', password='pass12345')
        resp = self.client.post(reverse('blog:post-delete', kwargs={'pk': self.post.pk}), follow=True)
        self.assertRedirects(resp, reverse('blog:post-list'))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

class CommentTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='author', password='pass12345')
        self.other = User.objects.create_user(username='other', password='pass12345')
        self.post = Post.objects.create(title='Test post', content='Content', author=self.author)

    def test_create_comment_requires_login(self):
        url = reverse('blog:comment-create', kwargs={'post_pk': self.post.pk})
        resp = self.client.post(url, {'content': 'Nice post!'})
        # should redirect to login
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username='other', password='pass12345')
        resp = self.client.post(url, {'content': 'Nice post!'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Comment.objects.filter(content='Nice post!', author=self.other, post=self.post).exists())

    def test_only_author_can_edit_comment(self):
        comment = Comment.objects.create(post=self.post, author=self.other, content='Hello')
        edit_url = reverse('blog:comment-update', kwargs={'post_pk': self.post.pk, 'pk': comment.pk})
        # anonymous
        resp = self.client.get(edit_url)
        self.assertNotEqual(resp.status_code, 200)
        # wrong user
        self.client.login(username='author', password='pass12345')
        resp = self.client.get(edit_url)
        # should be forbidden (403) or redirect depending on mixin behavior; check for non-200
        self.assertNotEqual(resp.status_code, 200)
        # correct user
        self.client.login(username='other', password='pass12345')
        resp = self.client.get(edit_url)
        self.assertEqual(resp.status_code, 200)

    def test_delete_comment(self):
        comment = Comment.objects.create(post=self.post, author=self.other, content='To delete')
        delete_url = reverse('blog:comment-delete', kwargs={'post_pk': self.post.pk, 'pk': comment.pk})
        self.client.login(username='other', password='pass12345')
        resp = self.client.post(delete_url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Comment.objects.filter(pk=comment.pk).exists())
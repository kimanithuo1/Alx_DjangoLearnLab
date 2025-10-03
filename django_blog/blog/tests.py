from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

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

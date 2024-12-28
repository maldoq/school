from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class LoginViewTestCase(TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()

         # Create an admin user
        self.admin_user = User.objects.create_superuser(
            username='admin_user',
            password='testpassword',
            email='admin@example.com'  # Provide a valid email
        )
        self.admin_user.save()

    def test_valid_admin_user_login(self):
        # Log in as an admin user
        self.client.login(username='admin_user', password='testpassword')
        response = self.client.get(reverse('login'))
        self.assertRedirects(response, '/admin/')

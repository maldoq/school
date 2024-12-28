from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from instructor.models import Instructor

class LoginViewTestCase(TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()

        self.instructor_user = User.objects.create_user(
            username='instructor_user', password='testpassword', email='instructor@example.com'
        )
        # Create and associate an Instructor instance
        self.instructor = Instructor.objects.create(user=self.instructor_user)

    def test_valid_instructor_user_login_with_username(self):
        # Log in as an instructor user
        self.client.login(username='instructor_user', password='testpassword')
        response = self.client.get(reverse('login'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_valid_instructor_user_login_with_email(self):
        # Log in as an instructor user
        self.client.login(email='instructor@example.com', password='testpassword')
        response = self.client.get(reverse('login'))
        self.assertRedirects(response, reverse('dashboard'))


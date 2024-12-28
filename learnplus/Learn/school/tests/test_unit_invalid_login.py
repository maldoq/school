from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from student.models import Student

class LoginViewTestCase(TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()

        # Create test users
        self.student_user = User.objects.create_user(
            username='student_user', password='testpassword', email='student@example.com'
        )
        # Create and associate a Student instance
        self.student = Student.objects.create(user=self.student_user)

    def test_invalid_login(self):
        # Attempt to log in with invalid credentials
        logged_in = self.client.login(username='invalid_user', password='wrongpassword')
        self.assertFalse(logged_in)
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/guest-login.html')


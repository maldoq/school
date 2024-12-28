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

    def test_empty_login(self):
        # Simulate a GET request when the user is not authenticated
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/guest-login.html')


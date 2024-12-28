from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from student.models import Student  # Adjust based on your actual student model import
from instructor.models import Instructor  # Adjust based on your actual instructor model import

class CartAndCoursesViewsTestCase(TestCase):

    def setUp(self):
        # Create a student and instructor user
        self.student_user = User.objects.create_user(
            username="studentuser", password="password123"
        )
        self.instructor_user = User.objects.create_user(
            username="instructoruser", password="password123"
        )

        # Create associated student and instructor models
        self.student = Student.objects.create(user=self.student_user)
        self.instructor = Instructor.objects.create(user=self.instructor_user)

    def test_cart_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-cart.html')
    
    def test_cart_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('cart'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_courses_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-courses.html')
    
    def test_courses_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('courses'))
        self.assertRedirects(response, reverse('dashboard'))

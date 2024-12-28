from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import MagicMock

# Mock models (replace with actual models if needed)
class MockStudentUser:
    def __init__(self, classe=None):
        self.classe = classe

class MockInstructor:
    pass

class MyCoursesTest(TestCase):
    
    def setUp(self):
        # Create test users
        self.student = User.objects.create_user(username='student', password='password')
        self.student.student_user = MockStudentUser(classe=1)
        
        self.instructor = User.objects.create_user(username='instructor', password='password')
        self.instructor.instructor = MockInstructor()
        
        self.client = Client()

    def test_my_courses_as_student(self):
        self.client.login(username='student', password='password')
        response = self.client.get(reverse('my_courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-my-courses.html')

    def test_my_courses_as_instructor(self):
        self.client.login(username='instructor', password='password')
        response = self.client.get(reverse('my_courses'))
        self.assertRedirects(response, reverse('dashboard'))

class QuizListTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user(username='student', password='password')
        self.student.student_user = MockStudentUser(classe=1)
        
        self.instructor = User.objects.create_user(username='instructor', password='password')
        self.instructor.instructor = MockInstructor()

        self.client = Client()

    def test_quiz_list_as_student(self):
        self.client.login(username='student', password='password')
        response = self.client.get(reverse('quiz_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-quiz-list.html')

    def test_quiz_list_as_instructor(self):
        self.client.login(username='instructor', password='password')
        response = self.client.get(reverse('quiz_list'))
        self.assertRedirects(response, reverse('dashboard'))

class ProfileTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user(username='student', password='password')
        self.student.student_user = MockStudentUser(classe=1)

        self.instructor = User.objects.create_user(username='instructor', password='password')
        self.instructor.instructor = MockInstructor()

        self.client = Client()

    def test_profile_as_student(self):
        self.client.login(username='student', password='password')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-profile.html')

    def test_profile_as_instructor(self):
        self.client.login(username='instructor', password='password')
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, reverse('dashboard'))

class ProfilePostsTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user(username='student', password='password')
        self.student.student_user = MockStudentUser(classe=1)

        self.instructor = User.objects.create_user(username='instructor', password='password')
        self.instructor.instructor = MockInstructor()

        self.client = Client()

    def test_profile_posts_as_student(self):
        self.client.login(username='student', password='password')
        response = self.client.get(reverse('profile_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-profile-posts.html')

    def test_profile_posts_as_instructor(self):
        self.client.login(username='instructor', password='password')
        response = self.client.get(reverse('profile_posts'))
        self.assertRedirects(response, reverse('dashboard'))

# Additional tests for other views (quiz_results, quizzes, statement) can follow a similar pattern

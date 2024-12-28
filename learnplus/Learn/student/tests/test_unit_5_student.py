from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Cours, Instructor, Student
from unittest.mock import patch

class TakeCourseTestCase(TestCase):
    
    def setUp(self):
        # Create a user and assign it to a student_user role
        self.user = User.objects.create_user(username="student", password="testpassword")
        self.student_user = Student.objects.create(user=self.user, classe_id=1)
        self.cours = Cours.objects.create(slug='course-slug', name='Test Course')
        self.instructor = Instructor.objects.create(user=self.user, classe_id=1)
        self.url = reverse('take_course', args=['course-slug'])

    @patch('django.contrib.auth.decorators.login_required')
    def test_take_course_authenticated_student(self):
        self.client.login(username="student", password="testpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')

    @patch('django.contrib.auth.decorators.login_required')
    def test_take_course_authenticated_instructor_redirect(self):
        self.client.login(username="student", password="testpassword")
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('dashboard'))

class TakeQuizTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="student", password="testpassword")
        self.student_user = Student.objects.create(user=self.user, classe_id=1)
        self.url = reverse('take_quiz')

    @patch('django.contrib.auth.decorators.login_required')
    def test_take_quiz_authenticated_student(self):
        self.client.login(username="student", password="testpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Take Quiz")

    @patch('django.contrib.auth.decorators.login_required')
    def test_take_quiz_authenticated_instructor_redirect(self):
        self.client.login(username="student", password="testpassword")
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('dashboard'))

class AccountEditTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="student", password="testpassword")
        self.student_user = Student.objects.create(user=self.user, classe_id=1)
        self.url = reverse('account_edit')

    @patch('django.contrib.auth.decorators.login_required')
    def test_account_edit_authenticated_student(self):
        self.client.login(username="student", password="testpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Account Edit")

    @patch('django.contrib.auth.decorators.login_required')
    def test_account_edit_authenticated_instructor_redirect(self):
        self.client.login(username="student", password="testpassword")
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('dashboard'))

class AccountEditTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="student", password="testpassword")
        self.student_user = Student.objects.create(user=self.user, classe_id=1)
        self.url = reverse('account_edit')

    @patch('django.contrib.auth.decorators.login_required')
    def test_account_edit_authenticated_student(self):
        self.client.login(username="student", password="testpassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Account Edit")

    @patch('django.contrib.auth.decorators.login_required')
    def test_account_edit_authenticated_instructor_redirect(self):
        self.client.login(username="student", password="testpassword")
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('dashboard'))


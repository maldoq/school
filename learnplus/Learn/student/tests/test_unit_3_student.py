from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from student.models import Student  # Adjust based on your actual student model import
from instructor.models import Instructor  # Adjust based on your actual instructor model import
from forum.models import Sujet  # Adjust based on your actual forum model import

class ViewsTestCase(TestCase):

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

    def test_earnings_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('earnings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-earnings.html')
    
    def test_earnings_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('earnings'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_forum_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('forum'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-forum.html')
    
    def test_forum_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('forum'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_forum_lesson_view_student(self):
        lesson = Sujet.objects.create(name="Lesson 1", slug="lesson-1")  # Create a dummy lesson
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('forum_lesson', kwargs={'slug': lesson.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-forum-lesson.html')
    
    def test_forum_lesson_view_instructor(self):
        lesson = Sujet.objects.create(name="Lesson 1", slug="lesson-1")  # Create a dummy lesson
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('forum_lesson', kwargs={'slug': lesson.slug}))
        self.assertRedirects(response, reverse('dashboard'))

    def test_forum_ask_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('forum_ask'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-forum-ask.html')
    
    def test_forum_ask_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('forum_ask'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_forum_thread_view_student(self):
        forum = Sujet.objects.create(name="Forum Thread 1", slug="forum-thread-1")  # Create a dummy forum thread
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('forum_thread', kwargs={'slug': forum.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-forum-thread.html')
    
    def test_forum_thread_view_instructor(self):
        forum = Sujet.objects.create(name="Forum Thread 1", slug="forum-thread-1")  # Create a dummy forum thread
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('forum_thread', kwargs={'slug': forum.slug}))
        self.assertRedirects(response, reverse('dashboard'))

    def test_help_center_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('help_center'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-help-center.html')
    
    def test_help_center_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('help_center'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_invoice_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('invoice'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-invoice.html')
    
    def test_invoice_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('invoice'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_messages_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('messages', kwargs={'classe': 1}))  # Assuming `classe` ID is 1
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-messages.html')
    
    def test_messages_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('messages', kwargs={'classe': 1}))  # Assuming `classe` ID is 1
        self.assertRedirects(response, reverse('dashboard'))

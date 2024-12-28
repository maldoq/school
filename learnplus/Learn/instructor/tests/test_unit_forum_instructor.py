from django.test import TestCase, Client
from django.contrib.auth.models import User
from school.models import Classe
from forum import models as forum_models
from instructor.models import Instructor
from django.urls import reverse


class ForumViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.index_student_url = reverse('index_student')

        # URLs
        self.forum_url = reverse('forum')
        self.forum_ask_url = reverse('forum_ask')
        self.forum_thread_url = lambda slug: reverse('forum_thread', kwargs={'slug': slug})

        # Create a student user
        self.student_user = User.objects.create_user(username='student', password='password123')
        self.student_user.student_user = True  # Assuming dynamic property
        self.student_user.save()

        # Create an instructor user
        self.instructor_user = User.objects.create_user(username='instructor', password='password123')
        self.classe = Classe.objects.create(name='Class A', status=True)
        self.instructor = Instructor.objects.create(
            user=self.instructor_user,
            contact='123456789',
            adresse='123 Test Street',
            bio='Instructor bio',
            classe=self.classe
        )

        # Create forum topics
        self.general_topic = forum_models.Sujet.objects.create(name="General Topic", slug="general", cours=None)
        self.class_topic = forum_models.Sujet.objects.create(
            name="Class Topic", slug="class", cours=None
        )

    def test_forum_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.forum_url)
        self.assertRedirects(response, self.index_student_url)

    def test_forum_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.forum_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-forum.html')
        self.assertIn('forum_general', response.context)
        self.assertIn('forum', response.context)
        self.assertEqual(len(response.context['forum_general']), 1)

    def test_forum_ask_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.forum_ask_url)
        self.assertRedirects(response, self.index_student_url)

    def test_forum_ask_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.forum_ask_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-forum-ask.html')

    def test_forum_thread_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.forum_thread_url(self.general_topic.slug))
        self.assertRedirects(response, self.index_student_url)

    def test_forum_thread_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.forum_thread_url(self.general_topic.slug))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-forum-thread.html')
        self.assertIn('forum', response.context)
        self.assertEqual(response.context['forum'].name, "General Topic")

    def test_redirects_unauthenticated_user(self):
        views_to_test = [
            self.forum_url,
            self.forum_ask_url,
            self.forum_thread_url(self.general_topic.slug),
        ]
        for url in views_to_test:
            response = self.client.get(url)
            self.assertRedirects(response, f"{self.login_url}?next={url}")

from django.test import TestCase, Client
from django.contrib.auth.models import User
from school.models import Chapitre, Classe, Cours
from chat.models import Salon
from django.urls import reverse
from django.utils.safestring import mark_safe
import json


class LessonAndMessagesViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.index_student_url = reverse('index_student')

        # URLs
        self.lesson_add_url = lambda slug: reverse('lesson_add', kwargs={'slug': slug})
        self.lesson_edit_url = lambda slug, id: reverse('lesson_edit', kwargs={'slug': slug, 'id': id})
        self.messages_url = lambda classe: reverse('messages', kwargs={'classe': classe})

        # Create a student user
        self.student_user = User.objects.create_user(username='student', password='password123')
        self.student_user.student_user = True  # Assuming dynamic property
        self.student_user.save()

        # Create an instructor user
        self.instructor_user = User.objects.create_user(username='instructor', password='password123')
        self.classe = Classe.objects.create(name='Class A', status=True)
        self.instructor_user.instructor = True  # Assuming dynamic property
        self.instructor_user.classe = self.classe
        self.instructor_user.save()

        # Create chapitre and cours
        self.chapitre = Chapitre.objects.create(name="Chapitre 1", slug="chapitre-1", classe=self.classe, status=True)
        self.cours = Cours.objects.create(name="Cours 1", slug="cours-1", chapitre=self.chapitre)

        # Create chat room
        self.salon = Salon.objects.create(classe=self.classe)

    def test_lesson_add_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.lesson_add_url(self.chapitre.slug))
        self.assertRedirects(response, self.index_student_url)

    def test_lesson_add_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.lesson_add_url(self.chapitre.slug))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-lesson-add.html')
        self.assertIn('chapitre', response.context)
        self.assertEqual(response.context['chapitre'].slug, self.chapitre.slug)

    def test_lesson_edit_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.lesson_edit_url(self.cours.slug, self.chapitre.id))
        self.assertRedirects(response, self.index_student_url)

    def test_lesson_edit_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.lesson_edit_url(self.cours.slug, self.chapitre.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-lesson-edit.html')
        self.assertIn('chapitre', response.context)
        self.assertIn('cours', response.context)
        self.assertEqual(response.context['chapitre'].id, self.chapitre.id)
        self.assertEqual(response.context['cours'].slug, self.cours.slug)

    def test_messages_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.messages_url(self.classe.id))
        self.assertRedirects(response, self.index_student_url)

    def test_messages_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.messages_url(self.classe.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-messages.html')
        self.assertIn('info_classe', response.context)
        self.assertIn('classe', response.context)
        self.assertIn('classe_json', response.context)
        self.assertIn('username', response.context)
        self.assertEqual(response.context['info_classe'].id, self.classe.id)
        self.assertEqual(response.context['classe'].id, self.salon.id)
        self.assertEqual(json.loads(response.context['username']), self.instructor_user.username)

    def test_redirects_unauthenticated_user(self):
        views_to_test = [
            self.lesson_add_url(self.chapitre.slug),
            self.lesson_edit_url(self.cours.slug, self.chapitre.id),
            self.messages_url(self.classe.id),
        ]
        for url in views_to_test:
            response = self.client.get(url)
            self.assertRedirects(response, f"{self.login_url}?next={url}")

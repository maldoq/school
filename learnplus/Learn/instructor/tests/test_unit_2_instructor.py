from django.test import TestCase, Client
from django.contrib.auth.models import User
from school.models import Matiere, Chapitre, Classe
from instructor.models import Instructor
from django.urls import reverse
from django.db.models import Q


class InstructorViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.index_student_url = reverse('index_student')

        # URLs
        self.course_add_url = reverse('course_add')
        self.courses_url = reverse('courses')
        self.earnings_url = reverse('earnings')
        self.matiere_url = lambda slug: reverse('matiere', kwargs={'slug': slug})
        self.course_edit_url = lambda slug: reverse('course_edit', kwargs={'slug': slug})

        # Create a student user
        self.student_user = User.objects.create_user(username='student', password='password123')
        self.student_user.student_user = True  # Assuming this is a dynamic property
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

        # Create matieres and chapitres
        self.matiere = Matiere.objects.create(name="Mathematics", slug="math", status=True)
        self.chapitre = Chapitre.objects.create(
            name="Algebra",
            slug="algebra",
            matiere=self.matiere,
            classe=self.classe,
            status=True
        )

    def test_course_add_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.course_add_url)
        self.assertRedirects(response, self.index_student_url)

    def test_course_add_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.course_add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-course-add.html')
        self.assertIn('matiere', response.context)
        self.assertEqual(len(response.context['matiere']), 1)

    def test_course_edit_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.course_edit_url(self.chapitre.slug))
        self.assertRedirects(response, self.index_student_url)

    def test_course_edit_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.course_edit_url(self.chapitre.slug))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-course-edit.html')
        self.assertIn('matiere', response.context)
        self.assertIn('chapitre', response.context)
        self.assertEqual(response.context['chapitre'].name, "Algebra")

    def test_courses_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.courses_url)
        self.assertRedirects(response, self.index_student_url)

    def test_courses_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.courses_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-courses.html')
        self.assertIn('Chapitre', response.context)
        self.assertEqual(len(response.context['Chapitre']), 1)

    def test_matiere_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.matiere_url(self.matiere.slug))
        self.assertRedirects(response, self.index_student_url)

    def test_matiere_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.matiere_url(self.matiere.slug))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-cours-chap.html')
        self.assertIn('Chapitre', response.context)
        self.assertEqual(len(response.context['Chapitre']), 1)

    def test_earnings_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.earnings_url)
        self.assertRedirects(response, self.index_student_url)

    def test_earnings_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.earnings_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-account-edit.html')

    def test_redirects_unauthenticated_user(self):
        views_to_test = [
            self.course_add_url,
            self.courses_url,
            self.earnings_url,
            self.matiere_url(self.matiere.slug),
            self.course_edit_url(self.chapitre.slug),
        ]
        for url in views_to_test:
            response = self.client.get(url)
            self.assertRedirects(response, f"{self.login_url}?next={url}")

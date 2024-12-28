from django.test import TestCase, Client
from django.contrib.auth.models import User
from school.models import Matiere
from instructor.models import Instructor
from django.urls import reverse


class DashboardViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.dashboard_url = reverse('dashboard')
        self.account_edit_url = reverse('account_edit')

        # Create a student user
        self.student_user = User.objects.create_user(username='student', password='password123')
        self.student_user.student_user = True  # Assuming `student_user` is a dynamic attribute
        self.student_user.save()

        # Create an instructor user
        self.instructor_user = User.objects.create_user(username='instructor', password='password123')
        self.instructor = Instructor.objects.create(
            user=self.instructor_user,
            contact='123456789',
            adresse='123 Test Street',
            bio='Instructor bio'
        )

        # Create matieres for the instructor view
        self.matiere1 = Matiere.objects.create(name="Mathematics", status=True)
        self.matiere2 = Matiere.objects.create(name="Physics", status=True)

    def test_dashboard_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.dashboard_url)
        self.assertRedirects(response, reverse('index_student'))

    def test_dashboard_renders_instructor_dashboard(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-dashboard.html')
        self.assertIn('matiere', response.context)
        self.assertEqual(len(response.context['matiere']), 2)

    def test_dashboard_redirects_unauthenticated_user(self):
        response = self.client.get(self.dashboard_url)
        self.assertRedirects(response, f"{self.login_url}?next={self.dashboard_url}")

    def test_account_edit_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.account_edit_url)
        self.assertRedirects(response, reverse('index_student'))

    def test_account_edit_renders_instructor_edit_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.account_edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-account-edit.html')

    def test_account_edit_redirects_unauthenticated_user(self):
        response = self.client.get(self.account_edit_url)
        self.assertRedirects(response, f"{self.login_url}?next={self.account_edit_url}")

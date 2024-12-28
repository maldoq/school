from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class ProfileAndQuizViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.index_student_url = reverse('index_student')

        # URLs
        self.profile_url = reverse('profile')
        self.quiz_edit_url = reverse('quiz_edit')
        self.quiz_add_url = reverse('quiz_add')
        self.quizzes_url = reverse('quizzes')
        self.review_quiz_url = reverse('review_quiz')

        # Create a student user
        self.student_user = User.objects.create_user(username='student', password='password123')
        self.student_user.student_user = True  # Assuming dynamic property
        self.student_user.save()

        # Create an instructor user
        self.instructor_user = User.objects.create_user(username='instructor', password='password123')
        self.instructor_user.instructor = True  # Assuming dynamic property
        self.instructor_user.save()

    def test_profile_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.profile_url)
        self.assertRedirects(response, self.index_student_url)

    def test_profile_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-profile.html')

    def test_quiz_edit_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.quiz_edit_url)
        self.assertRedirects(response, self.index_student_url)

    def test_quiz_edit_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.quiz_edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-quiz-edit.html')

    def test_quiz_add_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.quiz_add_url)
        self.assertRedirects(response, self.index_student_url)

    def test_quiz_add_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.quiz_add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-quiz-add.html')

    def test_quizzes_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.quizzes_url)
        self.assertRedirects(response, self.index_student_url)

    def test_quizzes_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.quizzes_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-quizzes.html')

    def test_review_quiz_redirects_student(self):
        self.client.login(username='student', password='password123')
        response = self.client.get(self.review_quiz_url)
        self.assertRedirects(response, self.index_student_url)

    def test_review_quiz_renders_instructor_page(self):
        self.client.login(username='instructor', password='password123')
        response = self.client.get(self.review_quiz_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-review-quiz.html')

    def test_redirects_unauthenticated_user(self):
        views_to_test = [
            self.profile_url,
            self.quiz_edit_url,
            self.quiz_add_url,
            self.quizzes_url,
            self.review_quiz_url,
        ]
        for url in views_to_test:
            response = self.client.get(url)
            self.assertRedirects(response, f"{self.login_url}?next={url}")

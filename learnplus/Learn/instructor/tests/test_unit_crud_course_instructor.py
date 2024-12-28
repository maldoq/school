from django.test import TestCase, Client
from django.contrib.auth.models import User
from school import models as school_models
from forum import models as forum_models
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class ViewTests(TestCase):

    def setUp(self):
        # Create a test user
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.instructor = school_models.Instructor.objects.create(user=self.user, bio="Test bio")
        self.user.student_user = False
        self.user.save()
        
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Create supporting data
        self.matiere = school_models.Matiere.objects.create(name="Math")
        self.chapitre = school_models.Chapitre.objects.create(
            titre="Test Chapitre",
            description="Description",
            matiere=self.matiere,
            classe=self.instructor.classe
        )

    def test_statement_view_as_instructor(self):
        response = self.client.get(reverse('statement'))  # Replace 'statement' with the actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/instructor-statement.html')

    def test_post_cours(self):
        response = self.client.post(reverse('post_cours'), {
            'title': 'New Chapter',
            'matiere': self.matiere.id,
            'date_debut': '2024-12-27',
            'date_fin': '2025-01-01',
            'description': 'A test description',
            'duration': 2,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

    def test_delete_chapitre(self):
        response = self.client.post(reverse('delete_chapitre'), {'id': self.chapitre.id})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

    def test_post_lesson(self):
        file = SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")
        response = self.client.post(reverse('post_lesson'), {
            'title': 'New Lesson',
            'chapitre': self.chapitre.id,
            'description': 'A lesson description',
            'file': file
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

    def test_delete_lesson(self):
        lesson = school_models.Cours.objects.create(
            titre="Test Lesson",
            description="Test Description",
            chapitre=self.chapitre
        )
        response = self.client.post(reverse('delete_lesson'), {'id': lesson.id})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

    def test_update_profile(self):
        response = self.client.post(reverse('update_profil'), {
            'nom': 'Updated LastName',
            'prenom': 'Updated FirstName',
            'email': 'updatedemail@example.com',
            'bio': 'Updated bio'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

    def test_update_password(self):
        response = self.client.post(reverse('update_password'), {
            'last_password': 'password123',
            'new_password': 'newpassword123',
            'confirm_password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

    def test_post_forum(self):
        response = self.client.post(reverse('post_forum'), {
            'titre': 'Forum Title',
            'question': 'Forum Question'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])


from django.test import TestCase
from django.contrib.auth.models import User
from school.models import Classe, Niveau
from instructor.models import Instructor


class InstructorModelTest(TestCase):
    
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        self.niveau = Niveau.objects.create()

        # Create a class
        self.classe = Classe.objects.create(numeroClasse=6)

        # Create an instructor
        self.instructor = Instructor.objects.create(
            user=self.user,
            contact='123456789',
            adresse='123 Test Street',
            classe=self.classe,
            bio='Test bio'
        )

    def test_slug_generation(self):
        # Check if slug is generated correctly
        self.assertEqual(self.instructor.slug, 'testuser')

    def test_instructor_creation(self):
        # Check if the instructor is created and linked correctly
        self.assertEqual(self.instructor.user.username, 'testuser')
        self.assertEqual(self.instructor.classe.nom, 'Test Class')
        self.assertEqual(self.instructor.contact, '123456789')
        self.assertEqual(self.instructor.adresse, '123 Test Street')
        self.assertEqual(self.instructor.bio, 'Test bio')
        self.assertTrue(self.instructor.status)

    def test_get_u_type_property(self):
        # Check the get_u_type property
        self.assertTrue(self.instructor.get_u_type)

    def test_default_values(self):
        # Check default values
        self.assertTrue(self.instructor.status)
        self.assertEqual(self.instructor.bio, 'Test bio')

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student
from school.models import Classe  # Assuming 'Classe' is in the 'school' app
from django.utils.text import slugify


class StudentModelTest(TestCase):
    def setUp(self):
        # Create a user instance for the Student model
        self.user = User.objects.create_user(
            username='john_doe',
            password='password123'
        )
        # Create a Classe instance for the student to be assigned
        self.classe = Classe.objects.create(nom='Class A', numeroClasse=101)
        
        # Create a Student instance
        self.student = Student.objects.create(
            user=self.user,
            classe=self.classe,
            photo=None,
            bio="Student bio description"
        )

    def test_student_creation(self):
        # Check that the student instance is created correctly
        self.assertEqual(self.student.user.username, "john_doe")
        self.assertEqual(self.student.classe.nom, "Class A")
        self.assertEqual(self.student.bio, "Student bio description")

    def test_slug_creation(self):
        # Verify the slug is created correctly based on the username
        expected_slug = slugify(self.student.user.username)
        self.assertEqual(self.student.slug, expected_slug)

    def test_student_string_representation(self):
        # Check the string representation of the student (should be the username)
        self.assertEqual(str(self.student), "john_doe")

    def test_get_u_type(self):
        # Test the get_u_type property
        # The student should return True for get_u_type, as the user is a student
        self.assertTrue(self.student.get_u_type)

    def test_get_u_type_no_student(self):
        # Create a new user without a corresponding student
        new_user = User.objects.create_user(username='jane_doe', password='password123')
        new_student = Student.objects.create(user=new_user, classe=self.classe, photo=None)
        
        # Test that the get_u_type property should return False for this new user
        self.assertFalse(new_student.get_u_type)

    def test_student_update(self):
        # Update a student's bio and save
        new_bio = "Updated bio description"
        self.student.bio = new_bio
        self.student.save()
        
        # Check if the bio has been updated
        self.assertEqual(self.student.bio, new_bio)

    def test_student_status_default(self):
        # Check that the default status is True
        self.assertTrue(self.student.status)

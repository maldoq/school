from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from school.models import Classe
from instructor.models import Instructor
from student.models import Student  # Adjust based on your actual student model import

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
        
        # Create a dummy class for student
        self.classe = Classe.objects.create(nom="Math Class", numeroClasse=101)

        # Add the student to a class
        self.student.classe = self.classe
        self.student.save()

    def test_index_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-dashboard.html')
    
    def test_index_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_payment_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('payment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-account-billing-payment-information.html')
    
    def test_payment_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('payment'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_subscription_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('subscription'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-account-billing-subscription.html')

    def test_subscription_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('subscription'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_upgrade_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('upgrade'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-account-billing-upgrade.html')

    def test_upgrade_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('upgrade'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_edit_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('edit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-account-edit.html')

    def test_edit_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('edit'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_edit_basic_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('edit_basic'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-account-edit-basic.html')

    def test_edit_basic_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('edit_basic'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_edit_profile_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-account-edit-profile.html')

    def test_edit_profile_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('edit_profile'))
        self.assertRedirects(response, reverse('dashboard'))

    def test_billing_view_student(self):
        self.client.login(username='studentuser', password='password123')
        response = self.client.get(reverse('billing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/fixed-student-billing.html')

    def test_billing_view_instructor(self):
        self.client.login(username='instructoruser', password='password123')
        response = self.client.get(reverse('billing'))
        self.assertRedirects(response, reverse('dashboard'))

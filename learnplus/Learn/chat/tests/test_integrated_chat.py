from django.test import TestCase
from django.contrib.auth.models import User
from school.models import Classe, Niveau  # Assuming this is where Classe is located
from chat.models import Salon, Message
from django.utils import timezone

class SalonModelTest(TestCase):
    """Tests for the Salon model and its signals"""

    def setUp(self):
        """Set up test environment"""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.niveau = Niveau.objects.create(nom="Licence 1")
        self.classe = Classe.objects.create(numeroClasse=3, niveau=self.niveau)
        self.salon = Salon.objects.create(nom="Salon A", classe=self.classe)

    def test_salon_creation(self):
        """Test that a Salon is created when a Classe is created"""
        self.assertEqual(Salon.objects.count(), 1)
        salon = Salon.objects.first()
        self.assertEqual(salon.nom, "Salon A")
        self.assertEqual(salon.classe, self.classe)

    def test_salon_auto_create_on_classe_creation(self):
        """Test the signal handler that automatically creates a Salon when a Classe is created"""
        new_classe = Classe.objects.create(nom="Classe 2")
        self.assertEqual(Salon.objects.count(), 2)  # one Salon should be created automatically
        salon = Salon.objects.get(classe=new_classe)
        self.assertIsNotNone(salon)

    def test_salon_date_add(self):
        """Test that the 'date_add' field is automatically populated"""
        self.assertIsNotNone(self.salon.date_add)

    def test_salon_status(self):
        """Test default status of Salon"""
        self.assertTrue(self.salon.status)

    def test_salon_update(self):
        """Test that the 'date_upd' field is updated when the Salon is saved"""
        initial_date_upd = self.salon.date_upd
        self.salon.nom = "Salon B"
        self.salon.save()
        self.assertNotEqual(self.salon.date_upd, initial_date_upd)

class MessageModelTest(TestCase):
    """Tests for the Message model"""

    def setUp(self):
        """Set up test environment"""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.classe = Classe.objects.create(nom="Classe 1")
        self.salon = Salon.objects.create(nom="Salon A", classe=self.classe)
        self.message = Message.objects.create(auteur=self.user, message="Test message", salon=self.salon)

    def test_message_creation(self):
        """Test that a message is created with correct data"""
        self.assertEqual(Message.objects.count(), 1)
        message = Message.objects.first()
        self.assertEqual(message.auteur, self.user)
        self.assertEqual(message.message, "Test message")
        self.assertEqual(message.salon, self.salon)

    def test_message_date_add(self):
        """Test that the 'date_add' field is automatically populated"""
        self.assertIsNotNone(self.message.date_add)

    def test_message_update(self):
        """Test that the 'date_update' field is updated when the Message is saved"""
        initial_date_update = self.message.date_update
        self.message.message = "Updated message"
        self.message.save()
        self.assertNotEqual(self.message.date_update, initial_date_update)

    def test_message_status(self):
        """Test default status of Message"""
        self.assertTrue(self.message.status)

class SignalTest(TestCase):
    """Tests for signals related to Salon model"""

    def setUp(self):
        """Set up test environment"""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.classe = Classe.objects.create(nom="Classe 1")

    def test_create_salon_signal(self):
        """Test the post_save signal for creating Salon"""
        initial_salon_count = Salon.objects.count()
        new_classe = Classe.objects.create(nom="Classe 2")
        self.assertEqual(Salon.objects.count(), initial_salon_count + 1)  # Salon should be created automatically
        salon = Salon.objects.get(classe=new_classe)
        self.assertIsNotNone(salon)

    def test_save_salon_signal(self):
        """Test the post_save signal for saving Salon"""
        salon = Salon.objects.create(nom="Salon B", classe=self.classe)
        initial_date_upd = salon.date_upd
        self.classe.nom = "Updated Classe"
        self.classe.save()  # Trigger the post_save signal
        salon.refresh_from_db()
        self.assertNotEqual(salon.date_upd, initial_date_upd)  # date_upd should be updated

from django.test import TestCase
from django.contrib.auth.models import User
from school.models import Cours, Niveau, Classe, Matiere, Chapitre
from forum.models import Sujet, Reponse
from datetime import datetime
from django.utils.text import slugify


class ForumModelsTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", email='user@example.com', password="password")

        # Create a test Niveau
        self.niveau = Niveau.objects.create(nom="Niveau 1")

        # Create a test Classe
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)

        # Create a test Matiere
        self.matiere = Matiere.objects.create(nom="Maths")

        # Create a test Chapitre
        self.chapitre = Chapitre.objects.create(
            classe=self.classe,
            matiere=self.matiere,
            titre="Chapitre 1",
            description="Introduction au chapitre 1"
        )

        # Create a test Cours
        self.cours = Cours.objects.create(
            titre="Cours 1",
            chapitre=self.chapitre,
            description="Description du cours 1"
        )

    def test_sujet_creation_and_slug_generation(self):
        # Create a Sujet instance
        sujet = Sujet.objects.create(
            user=self.user,
            cours=self.cours,
            question="What is Django?",
            titre="Django Framework",
        )
        # Verify the instance is created
        self.assertEqual(Sujet.objects.count(), 1)
        self.assertEqual(sujet.titre, "Django Framework")
        self.assertEqual(
            sujet.slug,
            '-'.join((slugify(sujet.titre), slugify(sujet.date_add))),
        )

    def test_reponse_creation_and_slug_generation(self):
        # Create a Sujet instance
        sujet = Sujet.objects.create(
            user=self.user,
            cours=self.cours,
            question="What is Django?",
            titre="Django Framework",
        )

        # Create a Reponse instance
        reponse = Reponse.objects.create(
            user=self.user,
            sujet=sujet,
            reponse="Django is a high-level Python web framework.",
        )
        # Verify the instance is created
        self.assertEqual(Reponse.objects.count(), 1)
        self.assertEqual(reponse.sujet, sujet)
        self.assertEqual(
            reponse.slug,
            '-'.join((slugify(sujet.titre), slugify(reponse.date_add))),
        )

    def test_sujet_string_representation(self):
        sujet = Sujet.objects.create(
            user=self.user,
            cours=self.cours,
            question="What is Django?",
            titre="Django Framework",
        )
        self.assertEqual(str(sujet), "Django Framework")

    def test_reponse_string_representation(self):
        sujet = Sujet.objects.create(
            user=self.user,
            cours=self.cours,
            question="What is Django?",
            titre="Django Framework",
        )
        reponse = Reponse.objects.create(
            user=self.user,
            sujet=sujet,
            reponse="Django is a high-level Python web framework.",
        )
        self.assertEqual(str(reponse), "Django Framework")

    def test_relationships(self):
        sujet = Sujet.objects.create(
            user=self.user,
            cours=self.cours,
            question="What is Django?",
            titre="Django Framework",
        )
        reponse = Reponse.objects.create(
            user=self.user,
            sujet=sujet,
            reponse="Django is a high-level Python web framework.",
        )
        self.assertEqual(sujet.user, self.user)
        self.assertEqual(reponse.sujet, sujet)
        self.assertEqual(reponse.user, self.user)

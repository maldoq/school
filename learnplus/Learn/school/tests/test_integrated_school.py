from django.test import TestCase
from .models import Matiere, Niveau, Classe, Chapitre, Cours
from datetime import datetime, timedelta

class MatiereModelTest(TestCase):
    def setUp(self):
        self.matiere = Matiere.objects.create(
            nom="Mathematics",
            description="Mathematics course description"
        )

    def test_matiere_creation(self):
        self.assertEqual(self.matiere.nom, "Mathematics")
        self.assertTrue(self.matiere.slug.startswith("mathematics"))

    def test_matiere_string_representation(self):
        self.assertEqual(str(self.matiere), "Mathematics")


class NiveauModelTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Level 1")

    def test_niveau_creation(self):
        self.assertEqual(self.niveau.nom, "Level 1")
        self.assertTrue(self.niveau.slug.startswith("level-1"))

    def test_niveau_string_representation(self):
        self.assertEqual(str(self.niveau), "Level 1")


class ClasseModelTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Level 1")
        self.classe = Classe.objects.create(
            niveau=self.niveau,
            numeroClasse=101
        )

    def test_classe_creation(self):
        self.assertEqual(self.classe.niveau, self.niveau)
        self.assertEqual(self.classe.numeroClasse, 101)

    def test_classe_string_representation(self):
        self.assertEqual(str(self.classe), "Level 1 101")


class ChapitreModelTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Level 1")
        self.classe = Classe.objects.create(
            niveau=self.niveau,
            numeroClasse=101
        )
        self.matiere = Matiere.objects.create(nom="Mathematics")
        self.chapitre = Chapitre.objects.create(
            classe=self.classe,
            matiere=self.matiere,
            titre="Introduction to Algebra",
            duree_en_heure=3,
            description="An introductory chapter on algebra.",
            date_debut=datetime.now().date(),
            date_fin=(datetime.now() + timedelta(days=30)).date()
        )

    def test_chapitre_creation(self):
        self.assertEqual(self.chapitre.titre, "Introduction to Algebra")
        self.assertEqual(self.chapitre.classe, self.classe)
        self.assertEqual(self.chapitre.matiere, self.matiere)
        self.assertTrue(self.chapitre.slug.startswith("introduction-to-algebra"))

    def test_chapitre_string_representation(self):
        self.assertEqual(str(self.chapitre), "Introduction to Algebra")


class CoursModelTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Level 1")
        self.classe = Classe.objects.create(
            niveau=self.niveau,
            numeroClasse=101
        )
        self.matiere = Matiere.objects.create(nom="Mathematics")
        self.chapitre = Chapitre.objects.create(
            classe=self.classe,
            matiere=self.matiere,
            titre="Introduction to Algebra",
            duree_en_heure=3
        )
        self.cours = Cours.objects.create(
            titre="Algebra Basics",
            chapitre=self.chapitre,
            description="A basic course on algebra."
        )

    def test_cours_creation(self):
        self.assertEqual(self.cours.titre, "Algebra Basics")
        self.assertEqual(self.cours.chapitre, self.chapitre)
        self.assertTrue(self.cours.slug.startswith("algebra-basics"))

    def test_cours_string_representation(self):
        self.assertEqual(str(self.cours), "Algebra Basics")

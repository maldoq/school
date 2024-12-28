from django.test import TestCase
from school.models import Cours, Chapitre  # Import your related models
from .models import Quiz, Devoir, Question, Reponse
from datetime import datetime, timedelta

class QuizModelTest(TestCase):
    def setUp(self):
        # Create related objects
        self.cours = Cours.objects.create(titre="Sample Course", description="Test Description")

        # Create Quiz
        self.quiz = Quiz.objects.create(
            date="2024-12-27",
            titre="Sample Quiz",
            cours=self.cours,
            temps=30,
        )

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.titre, "Sample Quiz")
        self.assertTrue(self.quiz.slug.startswith("sample-quiz"))
        self.assertEqual(self.quiz.cours, self.cours)

    def test_quiz_string_representation(self):
        self.assertEqual(str(self.quiz), "2024-12-27")


class DevoirModelTest(TestCase):
    def setUp(self):
        # Create related objects
        self.chapitre = Chapitre.objects.create(titre="Sample Chapter", description="Test Chapter")

        # Create Devoir
        self.devoir = Devoir.objects.create(
            sujet="Sample Subject",
            dateDebut=datetime.now(),
            dateFermeture=datetime.now() + timedelta(days=5),
            chapitre=self.chapitre,
            coefficient=2,
            support="path/to/file.pdf",
        )

    def test_devoir_creation(self):
        self.assertEqual(self.devoir.sujet, "Sample Subject")
        self.assertTrue(self.devoir.slug.startswith("sample-subject"))
        self.assertEqual(self.devoir.chapitre, self.chapitre)

    def test_devoir_string_representation(self):
        self.assertEqual(str(self.devoir), "Sample Chapter")


class QuestionModelTest(TestCase):
    def setUp(self):
        # Create related objects
        self.cours = Cours.objects.create(titre="Sample Course", description="Test Description")
        self.quiz = Quiz.objects.create(
            date="2024-12-27",
            titre="Sample Quiz",
            cours=self.cours,
            temps=30,
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            question="Sample Question?",
            point=5,
            typequestion="qcm",
        )

    def test_question_creation(self):
        self.assertEqual(self.question.question, "Sample Question?")
        self.assertEqual(self.question.point, 5)
        self.assertEqual(self.question.typequestion, "qcm")
        self.assertEqual(self.question.quiz, self.quiz)

    def test_question_string_representation(self):
        self.assertEqual(str(self.question), "Sample Quiz")


class ReponseModelTest(TestCase):
    def setUp(self):
        # Create related objects
        self.cours = Cours.objects.create(titre="Sample Course", description="Test Description")
        self.quiz = Quiz.objects.create(
            date="2024-12-27",
            titre="Sample Quiz",
            cours=self.cours,
            temps=30,
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            question="Sample Question?",
            point=5,
            typequestion="qcm",
        )
        self.reponse = Reponse.objects.create(
            reponse="Sample Answer",
            question=self.question,
            is_True=True,
        )

    def test_reponse_creation(self):
        self.assertEqual(self.reponse.reponse, "Sample Answer")
        self.assertTrue(self.reponse.is_True)
        self.assertEqual(self.reponse.question, self.question)

    def test_reponse_string_representation(self):
        self.assertEqual(str(self.reponse), "Sample Answer")

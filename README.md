# Plateforme "Online School" pour la Gestion et Collaboration Éducative

## Présentation du Projet

Le projet **"Online School"** vise à développer une plateforme d’e-learning pour la gestion des processus éducatifs et la collaboration entre enseignants, étudiants et administrateurs. Cette plateforme permet la gestion des classes, matières, évaluations et la publication de contenus pédagogiques, tout en offrant des outils de communication comme des forums et des chats.

### Fonctionnalités Principales

- **Administrateur** : Gestion des utilisateurs, classes, matières, et inscriptions.
- **Enseignant** : Publication de cours, création de quiz/devoirs, gestion de forums.
- **Étudiant** : Accès aux cours, participation aux forums, visualisation des notes.
- **Collaboration** : Forums, chat de classe, et chat privé B2B.
- **Évaluations** : Quiz et devoirs, avec suivi des résultats et correction.

### Objectif TAF

Compléter, déboguer et améliorer la plateforme en ajoutant les fonctionnalités manquantes, en corrigeant les erreurs existantes et en appliquant des tests rigoureux (unitaires, d’intégration, fonctionnels).

### Livrables Attendus

- Version corrigée et améliorée de la plateforme.
- Documentation détaillant les bugs corrigés et les nouvelles fonctionnalités.
- Suite de tests automatisés avec leurs résultats.
- Rapport de validation des tests.

### Critères d’Évaluation

- Qualité du débogage, implémentation complète des fonctionnalités, robustesse des tests, respect des bonnes pratiques de développement et de documentation.

## Initialisation du Projet

Pour initialiser le projet, suivez les étapes ci-dessous :

1. **Clonez le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/online-school.git
   cd online-school

2. **Créez un environnement virtuel :** :
   ```bash
   python3.10 -m venv env

3. **Clonez le dépôt** :

 - Sur Windows :
   ```bash
   .\env\Scripts\activate
 - Sur macOS/Linux :
   ```bash
   source env/bin/activate

4. **Installez les dépendances :** :
   ```bash
   pip install -r requirements.txt

5. **Lancez le serveur Django :** :
   ```bash
   python manage.py runserver

## Liste des Fonctionnalités

Découvrez les fonctionnalités clés de notre solution, soigneusement conçues pour répondre aux besoins de chaque utilisateur :

### Administrateur

L’administrateur dispose d’un contrôle complet pour gérer efficacement le système :

- **Gestion des ressources académiques** : création et administration des filières, niveaux, classes, étudiants, enseignants et matières.
- **Attribution des responsabilités** : affectation des matières aux enseignants.
- **Inscription facilitée** : gestion des inscriptions des étudiants dans leurs classes respectives.

### Enseignant

Un espace dédié pour permettre aux enseignants de partager et organiser leurs savoirs :

- **Connexion sécurisée** : accès personnel à leur compte.
- **Gestion des contenus** : organisation des cours par chapitres et leçons, publication de contenus pédagogiques (texte, images, PDF, vidéos).
- **Interaction avec les étudiants** : création de forums pour faciliter les discussions.
- **Évaluation des connaissances** : ajout de quiz pour tester les compétences des apprenants.

### Étudiant

Une plateforme intuitive pour accompagner les étudiants dans leur apprentissage :

- **Accès aux cours** : connexion sécurisée pour explorer les contenus mis à disposition.
- **Participation active** : intégration dans les forums pour échanger avec les enseignants et les camarades.

## Tests Réalisés

Des tests rigoureux ont été effectués sur l'application web pour garantir la qualité et la fiabilité des fonctionnalités. Les tests incluent :

- **Tests unitaires** : vérification des fonctions et méthodes individuelles.
- **Tests d'intégration** : validation des interactions entre différents modules.
- **Tests fonctionnels** : évaluation des fonctionnalités de l'application du point de vue de l'utilisateur.

Chaque test a été documenté, et les résultats sont disponibles dans la documentation du projet.

---

Nous vous remercions de votre intérêt pour notre projet **"Online School"**. Pour toute question ou suggestion, n'hésitez pas à nous contacter !

from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from school import models as school_models
from quiz import models as quiz_models
from forum import models as forum_models
from chat import models as chat_models
from . import models
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse 
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required(login_url = 'login')
def dashboard(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    matiere = school_models.Matiere.objects.filter(status=True)
                    datas = {
                        'matiere':matiere,
                    }
                    return render(request,'pages/instructor-dashboard.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    
 


@login_required(login_url = 'login')
def account_edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/instructor-account-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    



# @login_required(login_url = 'login')
# def browse_courses(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                 return render(request,'pages/instructor-browse-courses.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")
    



@login_required(login_url = 'login')
def course_add(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student') 
            except Exception as e:
                print(e)
                print("2")

                if request.user.instructor:
                    matiere = school_models.Matiere.objects.filter(status=True)
                    datas = {
                        'matiere':matiere,
                    }
                    return render(request,'pages/instructor-course-add.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")



@login_required(login_url = 'login')
def course_edit(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")

                if request.user.instructor:
                    matiere = school_models.Matiere.objects.filter(status=True)
                    chapitre = school_models.Chapitre.objects.get(slug=slug)

                    datas = {
                        'matiere':matiere,
                        'chapitre':chapitre,
                    }
                    return render(request,'pages/instructor-course-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





@login_required(login_url = 'login')
def courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student') 
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    Chapitre = school_models.Chapitre.objects.filter(Q(status=True) & Q(classe=request.user.instructor.classe))
                    datas = {
                            'Chapitre' : Chapitre ,
                           }
                    return render(request,'pages/instructor-courses.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





@login_required(login_url = 'login')
def matiere(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    Chapitre = school_models.Chapitre.objects.filter(Q(status=True) & Q(classe=request.user.instructor.classe) & Q(matiere__slug=slug))
                    datas = {
                            'Chapitre' : Chapitre ,
                           }
                    return render(request,'pages/instructor-cours-chap.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")



@login_required(login_url = 'login')
def earnings(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-account-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





# @login_required(login_url = 'login')
# def edit_invoice(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-edit-invoice.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")





@login_required(login_url = 'login')
def forum(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    forum_general = forum_models.Sujet.objects.filter(cours=None)
                    forum = forum_models.Sujet.objects.filter(cours__chapitre__classe=request.user.instructor.classe)
                    datas = {
                        'forum_general': forum_general,
                        'forum': forum,
                    }
                    return render(request,'pages/instructor-forum.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    




@login_required(login_url = 'login')
def forum_ask(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-forum-ask.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    




@login_required(login_url = 'login')
def forum_thread(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    forum = forum_models.Sujet.objects.get(slug=slug)
                    datas = {
                        "forum": forum,
                    }
                    return render(request,'pages/instructor-forum-thread.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





# @login_required(login_url = 'login')
# def invoice(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-invoice.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")
    





# @login_required(login_url = 'login')
# def invoice_settings(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-invoice-settings.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")
    





@login_required(login_url = 'login')
def lesson_add(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    chapitre = school_models.Chapitre.objects.get(slug=slug)
                    datas = {
                        'chapitre': chapitre,
                           }
                    return render(request,'pages/instructor-lesson-add.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")



@login_required(login_url = 'login')
def lesson_edit(request, slug, id):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    chapitre = school_models.Chapitre.objects.get(id=id)
                    cours = school_models.Cours.objects.get(slug=slug)

                    datas = {
                        'chapitre': chapitre,
                        'cours': cours,
                    }
                    return render(request,'pages/instructor-lesson-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





@login_required(login_url = 'login')
def messages(request, classe):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    exist_classe = chat_models.Salon.objects.get(classe=request.user.instructor.classe)
                    info = school_models.Classe.objects.get(id=request.user.instructor.classe.id)
                    user_room = ''                    
                    print(user_room)
                    datas = {
                        'info_classe': info,
                        'classe': exist_classe,
                        'classe_json': mark_safe(json.dumps(exist_classe.id)),
                        'username': mark_safe(json.dumps(request.user.username))
                    }
                    return render(request,'pages/instructor-messages.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
   




@login_required(login_url = 'login')
def messages_2(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-messages-2.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")






# @login_required(login_url = 'login')
# def my_courses(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-my-courses.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
  





@login_required(login_url = 'login')
def profile(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-profile.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





@login_required(login_url='login')
def quiz_edit(request, quiz_slug):
    if request.user.is_authenticated:
        try:
            if request.user.student_user:
                return redirect('index_student')
        except Exception as e:
            print(e)

        if request.user.instructor:
            # Fetch the quiz instance based on the slug
            quiz = get_object_or_404(quiz_models.Quiz, slug=quiz_slug)
            courses = school_models.Cours.objects.filter(status=True)

            if request.method == 'POST':
                # Handle the form submission
                titre = request.POST.get('titre')
                cours_id = request.POST.get('cours')
                image = request.FILES.get('image')  # Handle the uploaded image
                temps = request.POST.get('temps')  # Duration in minutes
                date = request.POST.get('date')  # Date of the quiz

                try:
                    # Fetch the course instance
                    cours = school_models.Cours.objects.get(id=cours_id)

                    # Update the quiz instance
                    quiz.titre = titre
                    quiz.cours = cours
                    quiz.temps = temps
                    quiz.date = date  # Update the date

                    # Handle the image if provided
                    if image:
                        quiz.image = image  # Update the image field

                    quiz.save()  # Save the updated quiz instance

                    return redirect('instructor-quizzes')  # Redirect to the quiz manager page
                except school_models.Cours.DoesNotExist:
                    return render(request, 'pages/instructor-quiz-edit.html', {'quiz': quiz, 'error': 'Course not found.'})
                except Exception as e:
                    print(e)
                    return render(request, 'pages/instructor-quiz-edit.html', {'quiz': quiz, 'error': 'An error occurred while saving the quiz.'})

            # If GET request, render the quiz edit form with existing data
            return render(request, 'pages/instructor-quiz-edit.html', {'quiz': quiz, 'courses':courses})

    return redirect("/admin/")




@login_required(login_url = 'login')
def quiz_add(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                courses = school_models.Cours.objects.filter(status=True)
                if request.user.instructor:
                    datas = {
                                'courses': courses,
                           }
                    return render(request,'pages/instructor-quiz-add.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url='login')
def post_quiz(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        cours_id = request.POST.get('cours')
        image = request.FILES.get('image')  # Handle the uploaded image
        temps = request.POST.get('temps')  # Duration in minutes
        date = request.POST.get('date')  # Date of the quiz

        try:
            # Fetch the course instance
            cours = school_models.Cours.objects.get(id=cours_id)

            # Create a new Quiz instance
            quiz = quiz_models.Quiz(
                titre=titre,
                cours=cours,
                date=date,  # Set the date from the form
                temps=temps,  # Set the duration
            )
            quiz.save()  # Save the quiz instance

            # Handle the image if needed
            if image:
                quiz.image = image  # Set the image field
                quiz.save()  # Save again to update the image

            return redirect('instructor-quizzes')  # Redirect to the quiz manager page
        except school_models.Cours.DoesNotExist:
            return render(request, 'pages/instructor-quiz-add.html', {'error': 'Course not found.'})
        except Exception as e:
            print(e)
            return render(request, 'pages/instructor-quiz-add.html', {'error': 'An error occurred while saving the quiz.'})




@login_required(login_url = 'login')
def quiz_results(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-quiz-results.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    




@login_required(login_url = 'login')
def quizzes(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    list_quiz = quiz_models.Quiz.objects.filter(Q(status=True) & Q(cours__chapitre__classe=request.user.instructor.classe))
                    datas = {
                            "list_quiz": list_quiz,
                           }
                    return render(request,'pages/instructor-quizzes.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





@login_required(login_url = 'login')
def review_quiz(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-review-quiz.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





# @login_required(login_url = 'login')
# def take_course(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-take-course.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")






# @login_required(login_url = 'login')
# def take_quiz(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-take-quiz.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")






# @login_required(login_url = 'login')
# def view_course(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-view-course.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")





@login_required(login_url = 'login')
def statement(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-statement.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

# fonction pour recuperer les donnees d'un cours et enregistrer

""" Add and update chapitre """
def post_cours(request):
    title = request.POST.get("title") 
    matiere = request.POST.get("matiere")
    date_fin = request.POST.get("date_fin")
    description = request.POST.get("description")
    date_debut = request.POST.get("date_debut")
    duration = request.POST.get("duration")
    id = request.POST.get("id")
    chapitre = ''

    try:
        chapitre = school_models.Chapitre.objects.get(id=id)
        chapitre.titre = title
        chapitre.duree_en_heure = duration
        chapitre.description = description
        matiere = school_models.Matiere.objects.get(id=int(matiere))
        chapitre.matiere = matiere
        chapitre.classe = request.user.instructor.classe
        chapitre.save()
        try:
            video = request.FILES["file"]
            image = request.FILES["image"]
            chapitre.video = video
            chapitre.image = image
            chapitre.save()
        except :
            pass
        try:
            chapitre.date_debut = date_debut
            chapitre.save()
        except:
            pass
        try:
            chapitre.date_fin = date_fin
            chapitre.save()
        except:
            pass
        success = True 
        message = 'mis à jour effectué  avec succés'
    except:
        chapitre = school_models.Chapitre()
        try:
            video = request.FILES["file"]
            image = request.FILES["image"]
            chapitre.video = video
            chapitre.image = image
            chapitre.save()
        except :
            pass
        chapitre.titre = title
        chapitre.duree_en_heure = duration
        chapitre.date_debut = date_debut
        chapitre.date_fin = date_fin
        chapitre.description = description
        matiere = school_models.Matiere.objects.get(id=int(matiere))
        chapitre.matiere = matiere
        chapitre.classe = request.user.instructor.classe
        chapitre.save()
        success = True 
        message = 'chapitre ajouté avec succés'
    data = {
        'success' : success,
        'message' : message,
        'slug': chapitre.slug,
    }
    return JsonResponse(data,safe=False)



""" delete chapitre"""
def delete_chapitre(request):
    id = request.POST.get("id")
    try:
        chapitre = school_models.Chapitre.objects.get(id=int(id))
        chapitre.delete()
        success = True
        message = "La leçon a bien été supprimée"
    except Exception as e:
        print(e)
        success = False
        message = "Une erreur s'est produite"
    data = {
        'success' : success,
        'message' : message,
    }
    return JsonResponse(data,safe=False)





""" add and update lesson """
def post_lesson(request):
    title = request.POST.get("title")
    chapitre = request.POST.get("chapitre")
    description = request.POST.get("description")
    id = request.POST.get("id")

    try:
        cours = school_models.Cours.objects.get(Q(id=int(id)) & Q(chapitre__id=int(chapitre)))

        try:
            video = request.FILES["file"]
            image = request.FILES["image"]
            pdf = request.FILES["pdf"]
            cours.video = video
            cours.image = image
            cours.pdf = pdf
        except:
            pass
        cours.titre = title
        cours.description = description
        cours.save()
        success = True 
        message = 'mis à jour effectué  avec succés'
    except:
        cours = school_models.Cours()
        try:
            chapitre = school_models.Chapitre.objects.get(id=int(chapitre))
            video = request.FILES["file"]
            image = request.FILES["image"]
            pdf = request.FILES["pdf"]
            cours.video = video
            cours.chapitre = chapitre
            cours.image = image
            cours.description = description
            cours.pdf = pdf
            cours.titre = title
            cours.save()
            success = True 
            message = 'cours ajouté avec succés'
        except Exception as e:
            print(e)
            success = False
            message = "Une erreur s'est produite"
    data = {
        'success' : success,
        'message' : message,
    }
    return JsonResponse(data,safe=False)



""" delete lesson"""
def delete_lesson(request):
    id = request.POST.get("id")
    try:
        lesson = school_models.Cours.objects.get(id=int(id))
        lesson.delete()
        success = True
        message = "La leçon a bien été supprimée"
    except Exception as e:
        success = False
        message = "Une erreur s'est produite"
    data = {
        'success' : success,
        'message' : message,
    }
    return JsonResponse(data,safe=False)

def update_profil(request):
    nom = request.POST.get("nom")
    prenom = request.POST.get("prenom")
    email = request.POST.get("email")
    bio = request.POST.get("bio")

    try:
        user = User.objects.get(username=request.user.username)
        user.last_name = nom
        user.first_name = prenom
        user.email = email
        user.save()
        instructor = models.Instructor.objects.get(user__id=request.user.id)
        instructor.bio = bio
        instructor.save()
        try:
            image = request.FILES["file"]
            instructor.photo = image 
            instructor.save()

        except:
            pass
        success = True 
        message = "vos informations ont été modifié avec succés"

    except:
        success = False
        message = "une erreur est subvenue lors de la mise à jour"
    data = {
        "success" : success,
        "message" : message,
        }
    return JsonResponse(data,safe=False)

        
def update_password(request):
    last_password = request.POST.get("last_password")
    new_password = request.POST.get("new_password")
    confirm_password = request.POST.get("confirm_password")

    try:
        if not request.user.check_password(last_password):
            success = False
            message = "Ancien mot de passe incorrect"
        elif new_password != confirm_password:
            success = False
            message = "Les mots de passe ne sont pas identiques"
        else:
            user = User.objects.get(username=request.user.username)
            username = user.username
            user.password = new_password
            user.set_password(user.password)
            user.save()
            user = authenticate(username=username, password=new_password)
            login(request, user)
            success = True 
            message = "Mot de passe modfifié avec succès"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la mise à jour"
    data = {
        "success" : success,
        "message" : message,
        }
    return JsonResponse(data,safe=False)

"""  Post forum """

def post_forum(request):
    titre = request.POST.get("titre")
    question = request.POST.get("question")
    val = ""
    try:
        forum = forum_models.Sujet()
        forum.titre = titre
        forum.question = question
        forum.user = request.user
        forum.save()
        val = forum.slug
        success = True 
        message = "Votre sujet a bien été ajouté!"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la soumission"
    data = {
        "success" : success,
        "message": message,
        "forum": val,
        }
    return JsonResponse(data,safe=False)

@login_required(login_url='login')
def post_response(request, question_id):
    if request.method == 'POST':
        # Get the response text from the form
        response_text = request.POST.get('comment')
        
        # Get the question instance
        question = get_object_or_404(forum_models.Sujet, id=question_id)

        # Create a new response instance
        response = forum_models.Reponse(
            reponse=response_text,
            sujet=question,
            user=request.user  # Set this based on your logic (e.g., if it's a correct answer)
        )
        response.save()  # Save the response to the database

        return redirect('instructor-forum')  # Redirect to the forum or the specific question page

    return redirect('instructor-forum')  # Redirect if the request method is not POST

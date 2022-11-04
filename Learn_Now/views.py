from django.http.response import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from django.urls import reverse
from django.db import IntegrityError
from .models import Quiz, Quiz_submitted, User, Course, Completed_class, Started_class, Course_Lectures, Assignments, Course_Unit

# Create your views here

def index(request):
    # index view only shows certain information depending if user is logged in
    if request.user.is_authenticated:
        user=request.user
        courses = Course.objects.all()
        user_started_courses = Started_class.objects.filter(students_enrolled=user)
        user_complet_courses = Completed_class.objects.filter(student_finished=user)
        units = Course_Unit.objects.all()
    else:
        courses = Course.objects.all()
        user=request.user
        user_started_courses = None
        user_complet_courses = None
        units = Course_Unit.objects.all()
       
    return render(request, "Learn_Now/index.html", {
        'user': user,
        'courses': courses,
        'user_st_courses': user_started_courses,
        'user_com_couses': user_complet_courses,
        'units': units,
    })


def about(request):
    return render(request, "Learn_Now/about.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(request, "Learn_Now/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "Learn_Now/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Learn_Now/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "Learn_Now/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        return render(request, "Learn_Now/register.html")
    
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required
def course_page(request, course_id):
    # used to show each course lecture and assignement
    user = request.user
    course = Course.objects.get(id=course_id)
    course_n = course.course_name
    lectures = Course_Lectures.objects.filter(course=course)
    assignments = Assignments.objects.filter(student=user, course=course)
    
    return render(request, "Learn_Now/course_page.html",{
        'course_id': course_id,
        'course_n': course_n,
        'course': course,
        'lectures': lectures,
        'user': user,
        'assignments': assignments,
    })

@csrf_exempt
@login_required
def dashboard_view(request):
    # show the users current courses and allow them to resume course or drop course
    user = request.user
    courses = Started_class.objects.filter(students_enrolled=user)
    comp_courses = Completed_class.objects.filter(student_finished=user)
    
    return render(request, "Learn_Now/dashboard.html", {
        'courses': courses,
        'comp_courses': comp_courses,
    })


@login_required    
def quiz(request, course_id, quiz_num):
    # shows the quizzes for each lecture in a course
    q_course = Course.objects.get(pk=course_id)
    course_name = q_course.course_name
    quiz_info = Quiz.objects.get(course=q_course, assign_num=int(quiz_num))
    
    if request.method == "POST":
        print("you submitted form")
    
    return render(request, "Learn_Now/quiz.html", {
        "course_id": course_id,
        "quiz_num": quiz_num,
        "q_course": q_course,
        "quiz_info": quiz_info,
        "course_name": course_name,
    })


@csrf_exempt
@login_required
def join(request, course_id):
    # this view is called by javascript function JoinCourse
    if request.method == "PUT":
        user = request.user
        
        # adds the user to the current_student list in Course
        course_s = Course.objects.get(pk=course_id)
        course_s.current_students.add(user)
        print( f"user joined course {course_id}")
        
        #creates and stores started course of the user
        s = Started_class(course=course_s, students_enrolled=user)
        s.save()
        
        # creates all the assignments needed for the user in the assignment table of database
        assign_num = course_s.num_assign
        for num in range(1,(assign_num+1)):
            new_assign = Assignments(student=user, course=course_s, assign_num=num, assign_score=0)
            new_assign.save()
        
        print("you started the Class")
        
        data = {
            'course_s_name': course_s.course_name, 
        }        
    return JsonResponse(data, safe=False)


@csrf_exempt
@login_required
def dropCourse(request, course_id):
    # this view is almost a reverse of the join view. It allows the user to drop a course.
    if request.method == "POST":
        user = request.user
        # removes user form current_student list in Course
        course_s = Course.objects.get(pk=course_id)
        course_s.current_students.remove(user)
        
        # delets the started course from database for the current user
        s = Started_class.objects.get(course=course_s, students_enrolled=user)
        s.delete()
        
        # deletes each of the assignments for the user in the current course being dropped
        assign_num = course_s.num_assign
        for num in range(1,(assign_num+1)):
            del_assign = Assignments.objects.get(student=user, course=course_s, assign_num=num)
            del_assign.delete()
        
        # deletes the quizzes that user may have been submitted by the user dropping the course
        del_quizes = Quiz_submitted.objects.filter(student=user, course=course_s)
        for quiz in del_quizes:
            quiz.delete()
        
        print("You have deleted the class")

        data = {
            'couse_d_name': course_s.course_name,
        }
    return JsonResponse(data, safe=False)

@login_required
def quiz_message(request, course_name, quiz_num):
    user=request.user
    course = Course.objects.get(course_name=course_name)
    course_id = course.id
    return render(request, "Learn_Now/quiz_message.html", {
        'course_id': course_id,
        'quiz_num': quiz_num,
        'user': user,
    })


@login_required
def save_quiz(request, course_name, quiz_num):
    
    #this saves the submmitted quiz to the database
    
    if request.method == "POST":
        course = Course.objects.get(course_name=course_name)
        user = request.user
        course_id = course.id
        course_started = Started_class.objects.get(course=course, students_enrolled=user)
        num_of_assign = course.num_assign
        print(request.POST)
        
        # Error checking to make sure the user has answered every question on the quiz
        if request.POST.get('quest_1') and request.POST.get('quest_2') and request.POST.get('quest_3') and request.POST.get('quest_4') and request.POST.get('quest_5'):
            sub_quiz=Quiz_submitted()
            num_correct = 0
            sub_quiz.student=user
            sub_quiz.course=course
            sub_quiz.assign_num=quiz_num
            
            # checks the quiz answeres from user against answer key from database
            answer_key = Quiz.objects.get(course=course, assign_num=quiz_num)
            
            sub_quiz.ans_1=request.POST.get('quest_1')
            if (str(answer_key.quest1_ans) == (sub_quiz.ans_1)):
                num_correct+=1
                
            sub_quiz.ans_2=request.POST.get('quest_2')
            if (str(answer_key.quest2_ans) == (sub_quiz.ans_2)):
                num_correct+=1
                
            sub_quiz.ans_3=request.POST.get('quest_3')
            if (str(answer_key.quest3_ans) == (sub_quiz.ans_3)):
                num_correct+=1   
                
            sub_quiz.ans_4=request.POST.get('quest_4')
            if (str(answer_key.quest4_ans) == (sub_quiz.ans_4)):
                num_correct+=1
            
            sub_quiz.ans_5=request.POST.get('quest_5')
            if (str(answer_key.quest5_ans) == (sub_quiz.ans_5)):
                num_correct+=1
            
            #saves the submitted quiz to the database
            sub_quiz.save()
            print(f"you subbmitted your quiz {quiz_num} for {course_name}")
        
            # calculates the grade of the quiz
            grade = num_correct*20
            quiz_grade = Assignments.objects.get(student=user, course=course, assign_num=quiz_num)
            quiz_grade.assign_score=grade
            quiz_grade.assign_completed=True
            quiz_grade.save()
            
            print(f"Number Correct = {num_correct}")
            print(f"Your grade is: {grade}")
            
            # checks if the last quiz is subbmitted and calculates final grade
            if num_of_assign == quiz_num:
                assignments = Assignments.objects.filter(student=user, course=course)
                total = 0
                for assign in assignments:
                    total = total + assign.assign_score
                final_grade = round(total/quiz_num)
                completed = Completed_class()
                completed.student_finished = user
                completed.class_completed = course_started
                completed.grade = final_grade
                completed.save()
                
                started = Started_class.objects.get(course=course, students_enrolled=user)
                started.completed=True
                started.save()
                
                course.students_completed.add(user)            
            
            return HttpResponseRedirect(reverse("course_page", args=(course_id,)))
        else:
            return HttpResponseRedirect(reverse("quiz_message", args=(course_name, quiz_num,)))

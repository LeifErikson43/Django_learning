from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("about", views.about, name="about"),
    path("course_page/<int:course_id>", views.course_page, name="course_page"),
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("quiz/<int:course_id>/<int:quiz_num>", views.quiz, name="quiz"),
    path("quiz_message/<str:course_name>/<int:quiz_num>", views.quiz_message, name="quiz_message"),
    
    #API Roots
    path("save_quiz/<str:course_name>/<int:quiz_num>", views.save_quiz, name="save_quiz"),
    path("join/<int:course_id>", views.join, name="join"),
    path("drop_course/<int:course_id>", views.dropCourse, name="dropCourse"),
    
    
]
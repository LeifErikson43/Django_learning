from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
import django.utils.timezone
from django.db.models.fields.reverse_related import ManyToOneRel

# Create your models here.

class User(AbstractUser):
    pass

class Course_Unit(models.Model):
    unit_name = models.CharField(max_length=100)
    unit_discription = models.CharField(max_length=400)
    
    def __str__(self):
        return f"Unit: {self.unit_name}"
    
class Course(models.Model):
    course_unit = models.ForeignKey("Course_Unit", on_delete=models.CASCADE, blank=True, null=True, default=None, related_name="course_unit")
    course_name = models.CharField(max_length=70)
    course_info = models.CharField(max_length=600, blank=True)
    num_assign = models.IntegerField(blank=True, default=3)
    intro_vid = models.URLField(max_length=220, blank=True)
    passed = models.BooleanField(blank=True, null=True)
    current = models.BooleanField(blank=True, null=True)
    future = models.BooleanField(blank=True, null=True)
    current_students = models.ManyToManyField(User, blank=True, related_name="current_students")
    students_completed = models.ManyToManyField(User, blank=True, related_name="students_completed")

    def __str__(self):
        return f"{self.id} : {self.course_name} number of assignments {self.num_assign}"

class Course_Lectures(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, related_name='Lecture_course')
    lecture_title = models.CharField(max_length=220, blank=True)
    lecture_num = models.IntegerField(blank=True)
    lecture_info = models.CharField(max_length=400, blank=True)
    lecture_vid = models.URLField(max_length=220, blank=True)
    lecture_assignment = models.BooleanField(default=False)


class Started_class(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE,default=None, blank=True, related_name='course_started')
    students_enrolled = models.ForeignKey('User', on_delete=models.CASCADE, default=None, blank=True, related_name='students_enrolled')
    completed = models.BooleanField(default=False)

class Assignments(models.Model):
    student = models.ForeignKey("User", on_delete=models.CASCADE, default=None, blank=True, related_name="assignment_student")
    course = models.ForeignKey("Course", on_delete=models.CASCADE, blank=True, related_name="assignment_course")
    assign_num = models.IntegerField(blank=True, null=True)
    assign_score = models.IntegerField(blank=True, null=True)
    assign_completed = models.BooleanField(default=False)

class Completed_class(models.Model):
    student_finished = ForeignKey('User', on_delete=models.CASCADE, blank=True, related_name='students_finished')
    class_completed = ForeignKey('Started_class',on_delete=models.CASCADE, blank=True, related_name='class_finished')
    grade = models.IntegerField(blank=True)
    completion_date = models.DateTimeField(default=django.utils.timezone.now)

class Quiz(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, related_name="course")
    assign_num = models.IntegerField(default=0)
    question_1 = models.CharField(max_length=300)
    quest1_ans = models.BooleanField()
    question_2 = models.CharField(max_length=300)
    quest2_ans = models.BooleanField()
    question_3 = models.CharField(max_length=300)
    quest3_ans = models.BooleanField()
    question_4 = models.CharField(max_length=300)
    quest4_ans = models.BooleanField()
    question_5 = models.CharField(max_length=300)
    quest5_ans = models.BooleanField()

    def __str__(self):
        return f"{self.id} for {self.course.course_name}"

class Quiz_submitted(models.Model):
    student = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, related_name="student")
    course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, related_name="quiz_course")
    assign_num = models.IntegerField(default=0)
    ans_1 = models.BooleanField()
    ans_2 = models.BooleanField()
    ans_3 = models.BooleanField()
    ans_4 = models.BooleanField()
    ans_5 = models.BooleanField()

    def __str__(self):
        return f"{self.id} for {self.course.course_name}"
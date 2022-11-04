from django.contrib import admin
from.models import Assignments, Course, Course_Lectures, Course_Unit, Quiz_submitted, User, Started_class, Completed_class, Quiz

# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Started_class)
admin.site.register(Completed_class)
admin.site.register(Quiz)
admin.site.register(Quiz_submitted)
admin.site.register(Course_Lectures)
admin.site.register(Assignments)
admin.site.register(Course_Unit)
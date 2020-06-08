from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .models import Student,Teacher,User,Dept,Course,Class,Assign,AttendenceClass 

class CourseAdmin(admin.ModelAdmin):
	list_display = ('id','name','dept')
	search_fields = ('id','name','dept')
	ordering = ['dept','id']
class AssignAdmin(admin.ModelAdmin):
	list_display = ('course','class_id','teacher')
	ordering = ['class_id__dept__name', 'class_id__id', 'course__id']
	raw_id_fields = ['course','class_id','teacher']
admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Dept)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Assign,AssignAdmin)
admin.site.register(AttendenceClass)


# Register your models here.

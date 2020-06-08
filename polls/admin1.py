from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .models import Student,Teacher,User,Dept,Course,Class,Assign 


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Dept)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Assign)

# Register your models here.

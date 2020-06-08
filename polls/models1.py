from django.contrib.auth.models import AbstractUser
from django.db import models
sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
day_of_week=(
    ('monday','monday'),
    ('tuesday','tuesday'),
    ('wednesday','wednesday'),
    ('thursday','thursday'),
    ('friday','friday'),
    ('saturday','saturday')
)

class User(AbstractUser):
    @property
    def is_student(self):
        if hasattr(self, 'student'):
            return True
        return False
    @property
    def is_teacher(self):
        if hasattr(self, 'teacher'):
            return True
        return False

class Dept(models.Model):
        id=models.CharField(primary_key=True,max_length=50)
        name=models.CharField(max_length=100)
        def __str__(self):
            return self.name 
class Teacher(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
        name = models.CharField(max_length=200)
        id = models.CharField(primary_key=True,max_length=100)
        dept = models.ForeignKey(Dept,on_delete=models.CASCADE,default=1)
        sex = models.CharField(max_length=10,choices=sex_choice,default='male')
        def __str__(self):
        	return self.name

class Course(models.Model):
        id=models.CharField(primary_key=True,max_length=100)
        name=models.CharField(max_length=100)
        shortname=models.CharField(max_length=50)
        dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
        def __str__(self):
            return self.name 
class Class(models.Model):
        id=models.CharField(primary_key=True,max_length=50)
        section=models.CharField(max_length=50)
        dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
        sem=models.IntegerField(default=1)
        class Meta:
            verbose_name_plural:'classes'
        def __str__(self):
            d=Dept.objects.get(name=self.dept)
            return '%s : %d %s' % (d.name,self.sem,self.section)

class Student(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
        name = models.CharField(max_length=200)
        roll_no = models.IntegerField(default=0)
        class_id = models.ForeignKey(Class,on_delete=models.CASCADE,default=1)
        father_name = models.CharField(max_length=100,default=1)
        sex = models.CharField(max_length=10,choices=sex_choice,default='male')
        def __str__(self):
            return self.name
class Assign(models.Model):
        course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
        class_id=models.ForeignKey(Class,on_delete=models.CASCADE)
        teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
        class Meta:
            unique_together=(('course_id','class_id','teacher_id'),)
        def __str__(self):
            cr=Course.objects.get(id=self.course_id)
            cl=Class.objects.get(id=self.class_id)
            tr=Teacher.objects.get(id=self.teacher_id)
            return '%s : %s : %s' % (cr.name,cl,tr.name)
class AssignDay(models.Model):
        assign=models.ForeignKey(Assign,on_delete=models.CASCADE)
        day=models.CharField(max_length=50,choices=day_of_week)

class AttendenceClass(models.Model):
        assign=models.ForeignKey(Assign,on_delete=models.CASCADE)
        date=models.DateField()
        status=models.IntegerField(default=0)

class Attendence(models.Model):
        student=models.ForeignKey(Student,on_delete=models.CASCADE)
        course=models.ForeignKey(Course,on_delete=models.CASCADE)
        status=models.BooleanField(default=True)
        attendenceclass=models.ForeignKey(AttendenceClass,on_delete=models.CASCADE,default=1)
        date=models.DateField(default='01-06-2020')
        def __str__(self):
            stt=Student.objects.get(name=self.student)
            cr=Course.objects.get(name=self.course)
            return '%s : %s' % (stt.name,cr.shortname)
def AttendenceTotal(self):
        student=models.ForeignKey(Student,on_delete=models.CASCADE)
        course=models.ForeignKey(Course,on_delete=models.CASCADE)
        class Meta:
            unique_together=(('student','course'),)
        @property
        def att_class(self):
            stud=Student.objects.filter(name=self.student)
            cr_id=Course.objects.filter(name=self.course)
            att_class=Attendence.objects.filter(student=stud,course=cr_id,status='True').count()
            return att_class 
        @property
        def att_total(self):
            stud=Student.objects.filter(name=self.student)
            cr_id=Course.objects.filter(name=self.course)
            att_total=Attendence.objects.filter(student=stud,course=cr_id).count()
            return att_total
        def attendence(self):
            stud=Student.objects.filter(name=self.student)
            cr=Course.objects.filter(name=self.course)
            att_cl=Attendence.objects.filter(student=stud,course=cr,status='True').count()
            ttotal_cl=Attendence.objects.filter(student=stud,course=cr).count()
            if(ttotal_cl == 0):
                attendence=0
            else:
                attendence=round(att_cl / ttotal_cl * 100,2)
            return attendence


    





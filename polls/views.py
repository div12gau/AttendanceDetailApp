from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from .models import Dept,Student,Teacher,Assign,Course,Class,AttendenceClass,Attendence,AttendenceTotal 
@login_required()
def index(request):
	if request.user.is_authenticated:
		if request.user.is_teacher:
			return render(request,'polls/t_homepage.html')
		if request.user.is_student:
			return render(request,'polls/home.html')
		return render(request,'polls/error.html')
	else:
		#return HttpResponse("nldfsesjla")
		return render(request,'polls/logout.html')

@login_required()
def attendance(request,stud_id):
	stud=Student.objects.get(roll_no=stud_id)
	#print(stud)
	assc=Assign.objects.filter(class_id=stud.class_id)
	#print(assc)
	att_list=[]
	for aa in assc:
		try:
			aat=AttendenceTotal.objects.get(student=stud,course=aa.course)
		except AttendenceTotal.DoesNotExist:
			aat=AttendenceTotal(student=stud,course=aa.course)
			aat.save()
		att_list.append(aat)
	return render(request,'polls/attendance.html',{'att_list':att_list})
	# print(att_list)
	# for aat in att_list:
	# 	print(aat.att_class)
	#return HttpResponse("nd hds kds")
@login_required()
def t_clas(request,teacher_id,choice):
	teacher1 = get_object_or_404(Teacher,id=teacher_id)
	#return HttpResponse("dshsdfkjdfhdfkh sdkfsh")
	return render(request,'polls/t_clas.html',{'teacher1':teacher1,'choice':choice})

@login_required()
def t_student(request, assign_id):
    ass=get_object_or_404(Assign,id=assign_id)
    print(assign_id)
    att_list = []
    for stud in ass.class_id.student_set.all():
        try:
            a = AttendenceTotal.objects.get(student=stud, course=ass.course)
        except AttendenceTotal.DoesNotExist:
            a = AttendenceTotal(student=stud, course=ass.course)
            a.save()
        att_list.append(a)
    return render(request, 'polls/t_students.html', {'att_list': att_list})
@login_required()
def t_attendance(request,ass_c_id):
	aa=get_object_or_404(AttendenceClass,id=ass_c_id)
	assgn=aa.assign
	clas=assgn.class_id
	context = {
			'aa':aa,
			'assgn':assgn,
			'clas':clas 
	}
	return render(request,'polls/t_attendance.html',context)	
@login_required()
def t_class_date(request,assign_id):
	ass=get_object_or_404(Assign,id=assign_id)
	print(ass)
	now=timezone.now()
	att_list=ass.attendenceclass_set.filter(date__lte=now).order_by('-date')
	return render(request,'polls/t_class_date.html',{'att_list':att_list})
@login_required()
def confirm(request,ass_c_id):
	#print(ass_c_id)
	#namew=request.POST.get('140','')
	#print(namew)
	# if(request.method == 'POST'):
	# 	print("post request is sent")
	# else:
	# 	print("no post request")
	aatt1=get_object_or_404(AttendenceClass,id=ass_c_id)
	assgn=aatt1.assign
	cr=assgn.course 
	clas=assgn.class_id
	# print(assgn)
	# print(cr)
	# print(clas)
	for i,s in enumerate(clas.student_set.all()):
		d=s.roll_no
		#print(d)
		status=request.POST.get(str(s.roll_no))
		#print(status)
		if(status == 'present'):
			status='True'
		else:
			status='False'
		if(aatt1.status == 1):
			try:
				aa=Attendence.objects.get(course=cr,student=s,attendenceclass=aatt1,date=aatt1.date)
				aa.status=status
				aa.save()
			except Attendence.DoesNotExist:
				aa=Attendence(course=cr,student=s,status=status,attendenceclass=aatt1,date=aatt1.date)
				aa.save()
		else:
			aa=Attendence(course=cr,student=s,status=status,attendenceclass=aatt1,date=aatt1.date)
			#aa.status=1
			aa.save()
			aatt1.status=1
			aatt1.save()
	return HttpResponseRedirect(reverse('t_class_date',args=(assgn.id,)))
@login_required()
def edit_att(request,ass_c_id):
	assc=get_object_or_404(AttendenceClass,id=ass_c_id)
	assgn=assc.assign
	cr=assgn.course
	att_list=Attendence.objects.filter(attendenceclass=assc,course=cr)
	context={
		'assc':assc,
		'att_list':att_list,
	}
	return render(request,'polls/t_edit_att.html',context)
def signup(request):
	if(request.method == 'POST'):
		form=UserCreationForm(request.POST)
		if(form.is_valid()):
			form.save()
			username=form.cleaned_data.get('username')
			raw_password=form.cleaned_data.get('password1')
			user=authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'polls/signup.html',{'form':form})
@login_required()
def t_attendance_detail(request,stud_id,course_id):
	stud=get_object_or_404(Student,roll_no=stud_id)
	cr=get_object_or_404(Course,id=course_id)
	att_list=Attendence.objects.filter(course=cr,student=stud).order_by('date')
	return render(request,'polls/t_att_detail.html',{'att_list':att_list,'cr':cr})
@login_required()
def change_attendance(request,att_id):
	aa=get_object_or_404(Attendence,id=att_id)
	aa.status=not aa.status
	aa.save()
	return HttpResponseRedirect(reverse('t_attendance_detail',args=(aa.student.roll_no,aa.course_id)))
@login_required()
def attendance_detail(request,stud_id,course_id):
	stud=get_object_or_404(Student,roll_no=stud_id)
	cr=get_object_or_404(Course,id=course_id)
	att_list=Attendence.objects.filter(student=stud,course=cr).order_by('date')
	return render(request,'polls/att_detail.html',{'att_list':att_list,'cr':cr})
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import redirect, render
from school import models
from django.contrib import messages
from django.views import View


  
# class based view
class home(View):

# Create your views here.
    def get(self, request):
        if 'principal' in request.session.keys():
            principal=models.principal.objects.get(pusername=request.session.get('principal'))
            return render(request, 'myschool/index.html', {'principal':principal})
        elif 'teacher'in request.session.keys():
            teacher=models.teacher.objects.get(tusername=request.session.get('teacher'))
            return render(request,'myschool/index.html', {'teacher':teacher})
        elif 'student' in request.session.keys():
            student=models.student.objects.get(susername=request.session.get('student'))
            return render(request, 'myschool/index.html', {'student':student})
        else:
            return render(request, 'myschool/index.html')

class login_principal(View):
    # LOGIN PRINCIPAL
    def post(self, request):
        d={}
        try:
            username=request.POST['username']
            password=request.POST['password']
            principal=models.principal.objects.get(pusername=username,ppassword=password)
       
            if principal:
                
                request.session['principal']=username
                d['principal']=principal
                print('iop'+principal.pusername)
           
                return HttpResponseRedirect('/')
        except:
            return HttpResponseRedirect('/')
class add_teacher(View):
   

    def post(self, request):
            try:
                if 'principal' in request.session.keys():
                    teacher=models.teacher()
                    teacher.tusername=request.POST['username']
                    teacher.tname=request.POST['name']
                    teacher.tpassword=request.POST['password']
                    teacher.tmob=request.POST['mob']
                    teacher.tgender=request.POST['gender']
                    teacher.tage=request.POST['age']
                    teacher.tdob=request.POST['dob']
                    teacher.tsub=request.POST['subject']
                    teacher.save()

                    return HttpResponseRedirect('/')
            except:
                return HttpResponseRedirect('/')
# ADD TEACHER

# LOGIN TEACHER
def login_teacher(request): 
    d={}
    try:
        username=request.POST['username']
        password=request.POST['password']
        teacher=models.teacher.objects.get(tusername=username,tpassword=password)

        if teacher:
            request.session['teacher']=username
            d['teacher']=teacher
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')
# REMOVE TEACHER
def remove_teacher(request):
    try:
        if 'principal' in request.session.keys():
            principal=models.principal.objects.get(pusername=request.session.get('username'))
            teacher=models.teacher.objects.get(tusername=request.POST['username'])
            teacher.delete()
            return HttpResponseRedirect('/')
    except:
        raise Http404

# ADD STUDENT
def add_student(request):
    try:
        if 'principal' in request.session.keys():
            student=models.student()
            
            student.sname=request.POST['name']
            student.susername=request.POST['username']
            student.spassword=request.POST['password']
            student.sgender=request.POST['gender']
            student.sage=request.POST['age']
            student.sdob=request.POST['dob']
            student.smob=request.POST['mob']
            student.sclass=request.POST['class']
            student.save()
            print('lpp')
            
            
            return HttpResponseRedirect('/')

        elif 'teacher' in request.session.keys():
            student=models.student()
            student.sname=request.POST['name']
            student.susername=request.POST['username']
            student.spassword=request.POST['password']
            student.sgender=request.POST['gender']
            student.sage=request.POST['age']
            student.sdob=request.POST['dob']
            student.smob=request.POST['mob']
            student.sclass=request.POST['class']
            student.save()
            print('lpp')
            
            
            return HttpResponseRedirect('/')
    except:
        return render(request, 'myschool/index.html',{'err':'Please login'})

# LOGIN STUDENT
def login_student(request):
    d={}
    try:
        username=request.POST['username']
        password=request.POST['password']
        student=models.student.objects.get(susername=username,spassword=password)

        if student:
            request.session['student']=username
            d['student']=student
            
            return HttpResponseRedirect('/')
    except:
        return render(request, 'myschool/index.html')   

# REMOVE STUDENT
def remove_student(request):
    try:
        if 'principal' in request.session.keys():
            try:
                student=models.student.objects.get(susername=request.POST['username'])
                student.delete()
                return HttpResponseRedirect('/')
            except:
                if 'teacher' in request.session.keys():
                    student=models.student.objects.get(susername=request.POST['username'])
                    student.delete()
                    return HttpResponseRedirect('/')
    except:
        raise Http404
# LOGOUT
def logout(request):
    if 'principal' in request.session.keys():
        del request.session['principal']
    elif 'teacher' in request.session.keys():
        del request.session['teacher']
    else:
        if 'student' in request.session.keys():
            del request.session['student']
    messages.success(request, 'Logout successfull')
    return redirect('/')
def about(request):
        if 'principal' in request.session.keys():
            principal=models.principal.objects.get(pusername=request.session.get('principal'))
            return render(request, 'myschool/about.html', {'principal':principal})
        elif 'teacher'in request.session.keys():
            teacher=models.teacher.objects.get(tusername=request.session.get('teacher'))
            return render(request,'myschool/about.html', {'teacher':teacher})
        elif 'student' in request.session.keys():
            student=models.student.objects.get(susername=request.session.get('student'))
            return render(request, 'myschool/about.html', {'student':student})
        else:
            return render(request, 'myschool/about.html')

def contact(request):
        if 'principal' in request.session.keys():
            principal=models.principal.objects.get(pusername=request.session.get('principal'))
            return render(request, 'myschool/contact.html', {'principal':principal})
        elif 'teacher'in request.session.keys():
            teacher=models.teacher.objects.get(tusername=request.session.get('teacher'))
            return render(request,'myschool/contact.html', {'teacher':teacher})
        elif 'student' in request.session.keys():
            student=models.student.objects.get(susername=request.session.get('student'))
            return render(request, 'myschool/contact.html', {'student':student})
        else:
            return render(request, 'myschool/contact.html')

def sclass(request):
        if 'principal' in request.session.keys():
            principal=models.principal.objects.get(pusername=request.session.get('principal'))
            return render(request, 'myschool/class.html', {'principal':principal})
        elif 'teacher'in request.session.keys():
            teacher=models.teacher.objects.get(tusername=request.session.get('teacher'))
            return render(request,'myschool/class.html', {'teacher':teacher})
        elif 'student' in request.session.keys():
            student=models.student.objects.get(susername=request.session.get('student'))
            return render(request, 'myschool/class.html', {'student':student})
        else:
            return render(request, 'myschool/class.html')

def notice(request):
    
        notice=models.notice.objects.all()
        if 'principal' in request.session.keys():
            principal=models.principal.objects.get(pusername=request.session.get('principal'))
            return render(request, 'myschool/notice.html', {'principal':principal,'notice':notice})
        elif 'teacher'in request.session.keys():
            teacher=models.teacher.objects.get(tusername=request.session.get('teacher'))
            return render(request,'myschool/notice.html', {'teacher':teacher,'notice':notice})
        elif 'student' in request.session.keys():
            student=models.student.objects.get(susername=request.session.get('student'))
            return render(request, 'myschool/notice.html', {'student':student,'notice':notice})
        else:
            return render(request, 'myschool/notice.html',{'notice':notice})

def add_notice(request):    
        return render(request, 'myschool/add_notice.html')

def get_notice(request):
        
        try:
            
            notice=models.notice()
            notice.date=request.POST['date']
            notice.slno=request.POST['notice_no']
            
            notice.title=request.POST['title']
            notice.body=request.POST['body']
            notice.save()
            return HttpResponseRedirect('notice')
        except:
            return render(request, 'myschool/add_notice.html')
   
from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')


def home(request):
    return render(request,'home.html')


def contactus(request):
    return render(request,'contactus.html')

def addquestion(request):
    return render(request,'addquestion.html')

def adminaddinstructor(request):
    return render(request,'adminaddinstructor.html')

def admineditinstructordetails(request):
    return render(request,'admineditinstructordetails.html')

def admineditstudent(request):
    return render(request,'admineditstudent.html')

def adminhome(request):
    return render(request,'adminhome.html')

def adminsettings(request):
    return render(request,'adminsettings.html')

def adminstudentmanage(request):
    return render(request,'adminstudentmanage.html')

def adminviewinstructor(request):
    return render(request,'adminviewinstructor.html')

def cvreport(request):
    return render(request,'cvreport.html')

def displayallimage(request):
    return render(request,'displayallimage.html')    

def displayquiz(request):
    return render(request,'displayquiz.html')    

def editinstructorprofile(request):
    return render(request,'editinstructorprofile.html')    

def imageoptiononlyview(request):
    return render(request,'imageoptiononlyview.html')

def imagequestion(request):
    return render(request,'imagequestion.html')

def imagequestionoptionadd(request):
    return render(request,'imagequestionoptionadd.html')    

def insteditstudent(request):
    return render(request,'insteditstudent.html')

def instmanagestudent(request):
    return render(request,'instmanagestudent.html')

def instructorhome(request):
    return render(request,'instructorhome.html')    

def instructorprofileview(request):
    return render(request,'instructorprofileview.html')    

def instsettings(request):
    return render(request,'instsettings.html')

def insttextcorpus(request):
    return render(request,'insttextcorpus.html')    

def login(request):
    return render(request,'login.html')

def onlyoptionadd(request):
    return render(request,'onlyoptionadd.html')

def onlyoptiondisplay(request):
    return render(request,'onlyoptiondisplay.html')    

def optionquestionimageview(request):
    return render(request,'optionquestionimageview.html')    

def prediction(request):
    return render(request,'prediction.html')

def profile(request):
    return render(request,'profile.html')    

def signup(request):
    return render(request,'signup.html')    

def quiz(request):
    return render(request,'quiz.html')    

def questionedit(request):
    return render(request,'questionedit.html')    

def questionpaper(request):
    return render(request,'questionpaper.html')

def questionselect(request):
    return render(request,'questionselect.html')    

def viewprofile(request):
    return render(request,'viewprofile.html')

def questionview(request):
    return render(request,'questionview.html')

def settings(request):
    return render(request,'settings.html')    
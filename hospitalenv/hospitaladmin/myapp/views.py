from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import appointment,Patientdb,doctorregdb,Department
from .forms import appontmentForm,doctorregForm,patientForm,contactform,departmentform
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request,'home.html')

def DoctorRegistration(req):
    dept=Department.objects.all()
    return render(req,'DoctorRegistration.html',{"dept":dept})

def PatientRegistration(request):
    if request.method=="POST":
        form=patientForm(request.POST)
        
        username=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken")
                return redirect(PatientRegistration)
            if form.is_valid():
                form.save()
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.success (request,"user created")
                return redirect('/')
        else:
            print("password mismatch")
        return redirect('/')
    else:
        return render(request,"PatientRegistration.html")
     


# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(usermodule)

#         else:
#             message = "Invalid username or password."
#             return render(request, 'login.html', {'message': message})
#     return render(request, 'login.html')


def Signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        try:
            user=Patientdb.objects.get(email=username,password=password)
            if user is not None:
                request.session['username']=username
                request.session['password']=password
                request.session['id']=user.id
                return redirect(usermodule)
            return render(request, 'login.html')
        except:
            pass
        
        try:
            user=doctorregdb.objects.get(email=username,password=password)
            if user is not None:
                request.session['username']=username
                request.session['password']=password
                request.session['id']=user.id
                return redirect(Doctormodule)
        except:
            message = "Invalid username or password."
            return render(request,'login.html', {'message': message})


        else:
            message = "Invalid username or password."
            return render(request, 'login.html', {'message': message})


    else:
        return render(request,'login.html')



def appointment1(request):
    data=doctorregdb.objects.all()

    if request.method=="POST":
        form= appontmentForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=appontmentForm()
        return render(request,"appointment.html",{"data":data})
    
def docreg(request):
    if request.method=="POST":
        form=doctorregForm(request.POST)
        print("helloooo")
        username=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken")
                return redirect(docreg)
            if form.is_valid():
                form.save()
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.success (request,"user created")
                return redirect('/')
        else:
            print("password mismatch")
        return redirect('/')
    else:
        return render(request,"DoctorRegistration.html")
    
def usermodule(req):
    return render(req,"userModule.html")

def contact(request):
    if request.method=="POST":
        form= contactform(request.POST)

        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=contactform()
        return render(request,"contact.html")


def departmentFn(request):
    if request.method == "POST":
        form = departmentform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"home.html")
    else :
        form = departmentform()
        return render(request,"Deptreg.html")
    
def show_dept(request):
    dept=Department.objects.all()
    return render(request,"departmentlist.html",{"dept":dept})
    
def Doctormodule(request):   
    return render(request,"DoctorModule.html")

def viewdoctors(request):
    data = doctorregdb.objects.all()
    return render(request,"view_Doctorlist.html",{"data":data})

def viewappointments(request,did):
    doc=doctorregdb.objects.get(id=did)
    dname=doc.doctorname
    data=appointment.objects.filter(doctorname=dname)
    return render(request,"view_appointemnts.html",{"data":data})

def logout(request):
    del request.session['username']
    del request.session['password']
    del request.session['id']
    return redirect(home)

def edit_patient(request,pk):
    user=Patientdb.objects.get(pk=pk)
    if request.method == "POST":
        form = patientForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(Signup)
    print(user.dob)
    context={
        "user":user,
    }
    return render(request,"edit_Patient.html",{"context":context})
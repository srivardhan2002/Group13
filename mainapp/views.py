from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *

def index(request):
    return render(request, "mainapp/index.html")

def stu_login(request):
    return render(request, "mainapp/stulogin.html")

def lib_login(request):
    return render(request, "mainapp/liblogin.html")

def lib(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        libSet = librarian.objects.all()
        is_there = False
        for f in libSet:
            if f.username == username and f.password == password:
                is_there = True
            if is_there:
                return HttpResponseRedirect(reverse('lib_home', kwargs={'lib':username}))

def lib_home(request, lib):
    libSet = librarian.objects.all()
    l = libSet.get(username = lib)
    return render(request, "mainapp/libhome.html",{
        "l": l
    })

def add(request, lib):
    if request.method == "POST":
        name = request.POST["name"]
        phoneno = request.POST["phoneNo"]
        email = request.POST["email"]
        enrollNo = request.POST["enrollNo"]
        username = request.POST["username"]
        password = request.POST["password"]
        p2 = request.POST["password2"]
        l = librarian.objects.get(username = lib)
        if password == p2:
            s = student(name=name, mobileNumber=phoneno, emailId=email, enrollmentNumber=enrollNo, username=username, password=password)
            s.save()
            return HttpResponseRedirect(reverse('add', kwargs={'lib': l.username}))
    else:
        l = librarian.objects.get(username = lib)
        return render(request, "mainapp/add.html", {
            "l": l
        })


def stu(request):

    if request.method == "POST":
        un = request.POST["username"]
        ps = request.POST["password"]
        stuSet = student.objects.all()
        is_there = False
        for f in stuSet:
            if f.username == un and f.password == ps:
                is_there = True
        if is_there:
            return HttpResponseRedirect(reverse('stu_home', kwargs={'stu': un}))

def stu_home(request, stu):
    s = student.objects.get(username = stu)
    return render(request, "mainapp/stuhome.html", {
        "s":s
    })

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        phoneno = request.POST["phoneNo"]
        email = request.POST["email"]
        enrollNo = request.POST["enrollNo"]
        username = request.POST["username"]
        password = request.POST["password"]
        p2 = request.POST["password2"]
        if password == p2:
            s = NewStudent(name=name, mobileNumber=phoneno, emailId=email, enrollmentNumber=enrollNo, username=username, password=password)
            s.save()
            return HttpResponseRedirect(reverse('register'))
    else:
        return render(request, "mainapp/register.html")

def requestList(request, lib):
    l = librarian.objects.get(username= lib)
    newStuSet = NewStudent.objects.all()
    return render(request, "mainapp/NewStuList.html", {
        "list": newStuSet,
        "l": l
    })

def add2(request, lib, stuId):
    if request.method == "POST":
        name = request.POST["name"]
        phoneno = request.POST["phoneNo"]
        email = request.POST["email"]
        enrollNo = request.POST["enrollNo"]
        username = request.POST["username"]
        password = request.POST["password"]
        s = student(name=name, mobileNumber=phoneno, emailId=email, enrollmentNumber=enrollNo, username=username, password=password)
        s.save()
        d = NewStudent.objects.get(id= stuId)
        d.delete()
        return HttpResponseRedirect(reverse('requestList', kwargs={'lib': lib}))
    else:
        l = librarian.objects.get(username=lib)
        s = NewStudent.objects.get(id = stuId)
        return render(request, "mainapp/add2.html",{
            "l": l, 
            "s": s
        })





    

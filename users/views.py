from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from . models import User

def index(request):
    return render(request,"users/index.html")
    

def home(request):
    usersList = User.objects.all()
    return render(request,"users/managerUser.html", {"users":usersList})

def adduser(request):
    id = request.POST['txtcod']
    name = request.POST['txtname']
    lastName = request.POST['txtlastname']
    email = request.POST['txtemail']
    password = request.POST['txtpassword']
    address = request.POST['txtaddress']
    workPlace = request.POST['txtwork']
    sex = request.POST['txtsex']

    user = User.objects.create(id = id, name = name, lastName = lastName, email = email,password = password, address = address, workPlace = workPlace, sex = sex)
    return redirect('/users/home')

def edituser(request, id):
    userList = User.objects.get(id = id)
    return render(request, "users/editUser.html", {"users":userList})

def editionuser(request):
    id = request.POST['txtcod']
    name = request.POST['txtname']
    lastName = request.POST['txtlastname']
    email = request.POST['txtemail']
    password = request.POST['txtpassword']
    address = request.POST['txtaddress']
    workPlace = request.POST['txtwork']
    sex = request.POST['txtsex']

    user = User.objects.get(id = id)
    
    user.name = name
    user.email = email
    user.password = password
    user.address = address
    user.workPlace = workPlace
    user.sex = sex
    user.save()
    return redirect('/users/home')
    
    
def deleteuser(request,id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('/users/home')
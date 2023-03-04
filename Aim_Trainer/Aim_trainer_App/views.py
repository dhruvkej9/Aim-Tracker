from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login

def index(request):
    # context = {
    #     'variable1' : 'Harry is great',
    #     'variable2' : 'rohan is great'
    # }
    # return render(request,'index.html',context)
    return render(request,'index.html')
    # return HttpResponse('this is homepage')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        # check if user has entered correct credentials 
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def signup(request):
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # user = User.objects.create_user(username = username,
    #                              email = email,
    #                              password = password)
    return render(request,'signup.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

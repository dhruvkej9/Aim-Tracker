from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
# from models import 
def index(request):
    # context = {
    #     'variable1' : 'Harry is great',
    #     'variable2' : 'rohan is great'
    # }
    # return render(request,'index.html',context)
    current_user = request.user
    if request.user.is_anonymous:
        return render(request,'index.html')
    return render(request,'index-login.html')
    # return HttpResponse('this is homepage')

def Signup(request):
    if request.method == "POST":
        submit = request.POST.get('submit')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        
        # while password != re_password:
        #     messages.success(request, 'Password Doesn\'t Match!')
        #     re_password = request.POST.get('re-password')
        if submit:
            user = User.objects.create_user(first_name = first_name,last_name = last_name,
                                            username = username,email = email,
                                            password = password)
            user.save()
            messages.success(request, 'Successfully Registered!')
            login(request, user)
            return redirect("/")
        else:
            return render(request,'login.html')
    return render(request,'signup.html')

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


def profile(request):
    current_user = request.user
    if request.user.is_anonymous:
        return redirect("/login")
    context = {"username" : current_user.username,"email" : current_user.email,
            "name" : current_user.first_name + ' ' + current_user.last_name}
    return render(request,'profile.html',context) 

def logoutUser(request):
    logout(request)
    return redirect("/")

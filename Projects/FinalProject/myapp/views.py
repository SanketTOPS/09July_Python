from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def login(request):
    if request.method=='POST':
        u_email=request.POST["email"]
        u_password=request.POST["password"]
        
        user=UserSignup.objects.filter(email=u_email,password=u_password)
        if user:
            print("Login Successfully!")
            request.session["user"]=u_email
            return redirect('/')
        else:
            print("Error!Login Faild...")
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    return render(request,'signup.html')

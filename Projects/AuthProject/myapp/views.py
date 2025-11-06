from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        em=request.POST['email']
        pa=request.POST['password']
        
        user=UserSignup.objects.filter(email=em,password=pa)
        if user:
            print("Login Successfully!")
            return redirect('home')
        else:
            print("Error!Login faild...")
        
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')
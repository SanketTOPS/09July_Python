from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def admin_login(request):
    if request.method=='POST':
        unm=request.POST["username"]
        pas=request.POST["password"]
        
        if unm=="admin" and pas=="admin@123":
            print("Login Successfull!")
            return redirect("admin_dashboard")
        else:
            print("Error!Invalid Login...")
    return render(request,'admin_login.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def admin_userdata(request):
    data=UserSignup.objects.all()
    return render(request,'admin_userdata.html',{'data':data})

def admin_notesdata(request):
    notesdata=mynotes.objects.all()
    return render(request,'admin_notesdata.html',{'notesdata':notesdata})

def admin_logout(request):
    return redirect("admin_login")
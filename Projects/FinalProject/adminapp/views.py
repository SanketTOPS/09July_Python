from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from datetime import datetime

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
    u=UserSignup.objects.all()
    n=mynotes.objects.all()
    totaluser=len(u)
    totalnotes=len(n)
    return render(request,'admin_dashboard.html',{'totaluser':totaluser,'totalnotes':totalnotes,'u':u})

def admin_userdata(request):
    data=UserSignup.objects.all()
    return render(request,'admin_userdata.html',{'data':data})

def admin_notesdata(request):
    notesdata=mynotes.objects.all()
    return render(request,'admin_notesdata.html',{'notesdata':notesdata})

def admin_logout(request):
    return redirect("admin_login")


def notes_approve(reuqest,id):
    nid=get_object_or_404(mynotes,id=id)
    nid.status="Approve"
    nid.updated_at=datetime.now()
    nid.save()
    
    #Email Sending Code
    
    return redirect('admin_notesdata')
    
def notes_reject(reuqest,id):
    nid=get_object_or_404(mynotes,id=id)
    nid.status="Reject"
    nid.updated_at=datetime.now()
    nid.save()
    
    #Email Sending Code
    
    return redirect('admin_notesdata')
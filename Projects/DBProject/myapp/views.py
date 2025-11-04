from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted!")
            return redirect('showdata')
        else:
            print(form.errors)
    return render(request,'index.html')

def showdata(request):
    data=Userdata.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    stid=Userdata.objects.get(id=id)
    if request.method=='POST':
        form=UserForm(request.POST,instance=stid)
        if form.is_valid():
            form.save()
            print("Record Updated!")
            return redirect('showdata')
        else:
            print(form.errors)
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=Userdata.objects.get(id=id)
    Userdata.delete(stid)
    return redirect('showdata')
    
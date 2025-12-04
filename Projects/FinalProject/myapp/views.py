from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from FinalProject import settings
from django.contrib.auth import logout

# Create your views here.
def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def login(request):
    if request.method=='POST':
        u_email=request.POST["email"]
        u_password=request.POST["password"]
        
        user=UserSignup.objects.filter(email=u_email,password=u_password)
        userid=UserSignup.objects.get(email=u_email)
        print(userid.id)
        if user:
            print("Login Successfully!")
            request.session["user"]=u_email
            request.session["userid"]=userid.id
            return redirect('/')
        else:
            print("Error!Login Faild...")
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            #OTP Email Sending
            global otp
            otp=random.randint(11111,99999)
            sub="Your OTP for Verification"
            mail_msg=f"Dear User\n\nThanks for registration with us!\nYour Email Verification code is {otp}.\nPlease verify your account and enjoy our services!\n\nThank & Regards\nNotesApp Team\n+91 9724799469 | sanket.tops@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            
            send_mail(subject=sub,message=mail_msg,from_email=from_ID,recipient_list=to_ID)
            return redirect('otpverify')
        else:
            print(form.errors)
    return render(request,'signup.html')


def otpverify(request):
    global otp
    msg=""
    if request.method=='POST':
        if otp==int(request.POST["otp"]):
            print("Verification Successfull")
            
            return redirect("login")
        else:
            msg="Sorry!Verfication faild....Try again!"
    return render(request,'otpverify.html',{'msg':msg})

def notes(request):
    user=request.session.get("user")
    cuser=UserSignup.objects.get(email=user)
    if request.method=='POST':
        form=NotesForm(request.POST,request.FILES)
        if form.is_valid():
            x=form.save(commit=False)
            x.status="Pending"
            x.user=cuser
            x.save()
            print("Notes Submitted Successfully!")
        else:
            print(form.errors)
    return render(request,'notes.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect("/")
    
def profile(request):
    uid=request.session.get("userid")
    user=UserSignup.objects.get(id=uid)
    if request.method=='POST':
        updateReq=SignupForm(request.POST,instance=user)
        if updateReq.is_valid():
            updateReq.save()
            print("Profile Updatetd!")
            return redirect("profile")
        else:
            print(updateReq.errors)
    return render(request,'profile.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        newContact=ContactForm(request.POST)
        if newContact.is_valid():
            newContact.save()
            
            #Success Email Sending
            
        else:
            print(newContact.errors)
    return render(request,'contact.html')
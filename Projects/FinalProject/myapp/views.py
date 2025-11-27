from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from FinalProject import settings

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
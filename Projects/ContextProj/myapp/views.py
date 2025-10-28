from django.shortcuts import render
import random

# Create your views here.
n=1
def index(request):
    name="Gopal"
    num=random.randint(1111,9999)
    global n
    n+=1
    return render(request,'index.html',{'name':name,'num':num,'n':n})
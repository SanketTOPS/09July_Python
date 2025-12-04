from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('login/',views.login,name='login'),
   path('signup/',views.signup,name='signup'),
   path('otpverify/',views.otpverify,name='otpverify'),
   path('notes/',views.notes,name='notes'),
   path('userlogout/',views.userlogout,name='userlogout'),
   path('profile/',views.profile,name='profile'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
]

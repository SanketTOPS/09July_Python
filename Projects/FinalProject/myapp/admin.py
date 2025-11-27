from django.contrib import admin
from .models import *

# Register your models here.

class UserData(admin.ModelAdmin):
    list_display=["id","fullname","email","password","mobile"]
admin.site.register(UserSignup,UserData)


class NotesData(admin.ModelAdmin):
    list_display=["id","uploaded_at","user","title","desc","subject","notes_file","status","updated_at"]
    
admin.site.register(mynotes,NotesData)

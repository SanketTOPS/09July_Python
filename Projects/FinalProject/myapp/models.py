from django.db import models

# Create your models here.

class UserSignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    mobile=models.BigIntegerField()

class mynotes(models.Model):
    uploaded_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(UserSignup,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    desc=models.TextField()
    subject=models.CharField(max_length=50)
    notes_file=models.FileField(upload_to='NotesData')
    status_opt=[
        ('Pending','Pending'),
        ('Approve','Approve'),
        ('Reject','Reject')
    ]
    status=models.CharField(max_length=20,choices=status_opt)
    updated_at=models.DateTimeField(blank=True,null=True)
    
    
class contactus(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    msg=models.TextField()

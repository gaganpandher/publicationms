from django.db import models
from userapp.models import UserRole

# Create your models here.
class FacultyInfo(models.Model):
    role_id=models.ForeignKey(UserRole,on_delete=models.CASCADE)
    teacher_name=models.CharField(max_length=200,default="")
    t_designation=models.CharField(max_length=200,default="")
    user_image1=models.CharField(max_length=500,null=True)
    email=models.CharField(max_length=200,default="",primary_key=True)
    mobile=models.BigIntegerField()
    isActive = models.BooleanField(default=False)
    otp = models.CharField(max_length=200, default="",null=True)
    token = models.CharField(max_length=200, default="",null=True)
    time = models.CharField(max_length=200, default="",null=True)
    password = models.CharField(max_length=200, default="")
    area_of_int=models.CharField(max_length=500,default="",null=True)
class PaperUpload(models.Model):
    role_id=models.ForeignKey(FacultyInfo,on_delete=models.CASCADE,default="1")
    paper_id=models.CharField(max_length=200,default="", primary_key=True)
    paper_upload=models.FileField()
    #email=models.ForeignKey(FacultyInfo,on_delete=models.CASCADE)
    paper_description=models.CharField(max_length=500,default="")
    author_name=models.CharField(max_length=200,default="")

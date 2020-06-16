from django.db import models

# Create your models here.
class UserRole(models.Model):
    role_id=models.CharField(max_length=200,primary_key=True)
    role_name=models.CharField(max_length=200,default="",unique=True)
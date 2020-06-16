from django import forms
from teachersapp.models import FacultyInfo,PaperUpload
from userapp.models import UserRole

class FacultyInfoForm(forms.ModelForm):
    class Meta():
        model=FacultyInfo
        exclude=["teacher_name","t_designation", "role"
                 "email","mobile","isActive","otp","token","time","password","user_image1","area_of_int"]

class PaperUploadForm(forms.ModelForm):
    class Meta():
        model=PaperUpload
        exclude=["paper_upload","paper_description","role_id","author_name","paper_id"]
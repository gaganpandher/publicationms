from django.shortcuts import render,HttpResponse,redirect
from userapp.models import UserRole
from userapp.forms import UserRoleForm
from teachersapp.models import FacultyInfo,PaperUpload
from teachersapp.forms import FacultyInfoForm,PaperUploadForm
#from miscellaneous import emailSending,otpGeneration

# Create your views here.
def userindex(request):
    data= FacultyInfo.objects.all()
    data1=TeacherId.objects.all()
    data2=PaperUpload.objects.all()
    return render(request,"userindex.html",{'teacherinfo':data,'paperinfo':data2})
def usergallery(request):
    return render(request,"usergallery.html")

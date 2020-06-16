from django.conf.urls import url
from userapp import views
app_name='userapp'
urlpatterns = [
    url(r'^index/$',views.userindex),
    url(r'^gallery/$',views.usergallery),
    #url(r'^usermaster/$',views.usmaster),
    #url(r'^login/$',views.login),
    #url(r'^updatepass/$',views.passwordUpdate),
  ]
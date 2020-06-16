from django import forms
from userapp.models import UserRole


class UserRoleForm(forms.ModelForm):
    class Meta():
        model=UserRole
        exclude=["role_id","role_name"]
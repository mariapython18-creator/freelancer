from django import forms
from .models import Job,CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Job_form(forms.ModelForm):
    class Meta:
        model = Job
        exclude= ['client']
class Register_Form(UserCreationForm):
        email = forms.EmailField(required=True)
        role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
        class Meta:
            model = CustomUser
            fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role']


class Login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
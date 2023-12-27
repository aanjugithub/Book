from django import forms
from book.models import Books

from django.contrib.auth.models import User


class BookForms(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "publisher":forms.TextInput(attrs={"class":"form-control"}),


        }

#registration form==inherit ---from 'django.contrib.auth',

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User  #user model is inheritted from user.auth class
        fields=["username","email","password"]
        #go to view page nd nimplement signupview
#login
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

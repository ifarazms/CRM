from django import forms
from django.forms import fields, models, TextInput

from .models import Lead, User
from django.contrib.auth.forms import UserCreationForm, UsernameField
# from django.contrib.auth import get_user_model


#User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
       model = Lead
       fields = ['first_name','last_name','age','agent']
       widgets = {
            'first_name':TextInput(attrs={
                'class':"flex ml-auto text-white bg-blue-500 border-0 py-2 px-6 focus:outline-none hover:bg-blue-600 rounded"
                }),
            'last_name':TextInput(attrs={
                'class':"flex ml-auto text-white bg-blue-500 border-0 py-2 px-6 focus:outline-none hover:bg-blue-600 rounded"
                }),
            'age':TextInput(attrs={
                'class':"flex ml-auto text-white bg-blue-500 border-0 py-2 px-6 focus:outline-none hover:bg-blue-600 rounded"
                }),
        }


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


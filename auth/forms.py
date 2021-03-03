from django import forms

class login(forms.Form):
    username=forms.CharField(min_length=4 ,max_length=20,label='Username',label_suffix=':-')
    password=forms.CharField(min_length=8 ,max_length=20 ,widget=forms.PasswordInput() ,label='Password',label_suffix=':-')
    
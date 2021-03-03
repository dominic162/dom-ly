from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from auth import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def auth_login(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect("/")
    context={
        'form':forms.login(),
    }
    if request.method=='POST':
        if 'login' in request.POST:
            data={
                'username':request.POST['username'],
                'password':request.POST['password']
            }
            form=forms.login(data)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    return HttpResponseRedirect("/")
                else:
                    context['error']='Invalid username or password'
            else:
                context['error']='Username length must be between 6-20. Password length must be between 8-20.'
        if 'signup' in request.POST:
            data={
                'username':request.POST['susername'],
                'password':request.POST['spassword']
            }
            form=forms.login(data)
            if form.is_valid():
                username=request.POST['susername']
                password=request.POST['spassword']
                cpassword=request.POST['cpassword']
                if password == cpassword:
                    try:
                        user=User.objects.get(username=username)
                        context['error']='User already exist'
                    except:
                        user=User.objects.create_user(username=username,password=password)
                        login(request,user)
                        return HttpResponseRedirect("/")
                else:
                    context['error']="Password and Confirm password doesn't match"
            else:
                context['error']='Username length must be between 6-20. Password length must be between 8-20.'
    return render(request,'login.html',context)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
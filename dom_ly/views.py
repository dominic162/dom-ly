from django.shortcuts import render
from django.http import request


def error(request):
    return render(request,'404.html')
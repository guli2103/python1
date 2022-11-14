from django.shortcuts import render
from frontend import *

def cars(request):
    return render(request,'index1.html')

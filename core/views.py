from django.shortcuts import render
from frontend import *

def video(request):
    return render(request, "index.html")

def ferrary(request):
    return render(request, "index1.html")

def cube(request):
    return render(request,"cube.html")    

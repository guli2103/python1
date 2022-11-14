from django.shortcuts import render
from frontend import *

def cube(request):
    return render(request,"cube.html")

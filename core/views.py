from django.shortcuts import render
from frontend import *

def video(request):
    return render(request, "index.html")
  

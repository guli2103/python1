
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cube/',include('cube.urls')),
    path('cars/',include('cars.urls')),
    
]

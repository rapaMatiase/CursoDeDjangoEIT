"""myfirstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('myapp2/', include('myapp2.urls')),
    path('clase2/', include('myapp_clase2.urls')),
    path('clase2bonus/', include('myapp_clas2_bonus.urls')),
    path('clase3/', include('myapp_clase3.urls')),
    path('clone/', include('google_forms_clone.urls'))
]

# path('aca puedeser cualquier valor/', include('<name_app>.ursl'))
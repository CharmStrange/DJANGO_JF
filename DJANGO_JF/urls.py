"""
URL configuration for DJANGO_JF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import animal_list, dokam_view, bunyangso_view, ipyangso_view, jarang_view

urlpatterns = [
    path('', animal_list, name='animal_list'),
    path('dokam/', dokam_view, name='dokam'),
    path('bunyangso/', bunyangso_view, name='bunyangso'),
    path('ipyangso/', ipyangso_view, name='ipyangso'),
    path('jarang/', jarang_view, name='jarang'),
]




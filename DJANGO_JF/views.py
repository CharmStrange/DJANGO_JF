from django.shortcuts import render
from .models import Animal

def animal_list(request):
    return render(request, 'animal_list.html')

def dokam_view(request):
    animals = Animal.objects.all()
    return render(request, 'dokam.html', {'animals': animals})

def bunyangso_view(request):
    animals = Animal.objects.all()
    return render(request, 'bunyangso.html', {'animals': animals})

def ipyangso_view(request):
    animals = Animal.objects.all()
    return render(request, 'ipyangso.html', {'animals': animals})

def jarang_view(request):
    animals = Animal.objects.all()
    return render(request, 'jarang.html', {'animals': animals})

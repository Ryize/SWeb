from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def register(request):
    users = User.objects.all()
    return render(request, 'authorize/register.html', {'users': users})

def about(request):
    return HttpResponse('<h1>About - о нас</h1>')
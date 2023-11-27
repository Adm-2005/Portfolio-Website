from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Skills, Certifications


def index(request):
    skills = Skills.objects.all()
    certifications = Certifications.objects.all()
    
    return render(request, 'index.html', context={'skills' : skills, 'certifications' : certifications})


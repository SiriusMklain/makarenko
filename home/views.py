from django.shortcuts import render
from .models import *


def home(request):
    projects = Project.objects.all().order_by('-date_pub')
    context = {
        'projects': projects
    }
    return render(request, 'home/index.html', context=context)

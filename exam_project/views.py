# exam_project/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
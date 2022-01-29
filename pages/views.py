from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request=request, template_name="pages/index.html")

def about(request):
    return render(request=request, template_name="pages/about.html")

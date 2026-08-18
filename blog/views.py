from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my blog 🚀")

def about(req):
    return render(req, 'about.html')

def detail(req, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(req, 'detail.html', {'blog': blog})

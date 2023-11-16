from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request, "portfolioapp/base.html")

def index(request):
    return render(request, "portfolioapp/index.html")
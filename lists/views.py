from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home_page(request):
    return render(request,'home.html')
from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home_page(request):
    if request.method == 'POST':
        return render(request,'home.html',{'new_item_text':request.POST.get('item_text','')})
            #HttpResponse(request.POST['item_text'])
    return render(request,'home.html')
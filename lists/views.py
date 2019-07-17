from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from lists.models import Item,List

def home_page(request):
    return render(request,'home.html')

def view_list(request):
    #print('i come to the view list')
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    #print('come to new ')
    list_=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/the_only_list_in_the_world/')


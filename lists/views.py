from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from lists.models import Item,List

def home_page(request):
    return render(request,'home.html')

def view_list(request,list_id):
    #print('i come to the view list')
    list_=List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    #print('come to new ')
    list_=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request,list_id):
    #print('welcome to add item')

    list_=List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect(f'/lists/{list_.id}/')


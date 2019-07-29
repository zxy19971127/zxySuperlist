from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^new$',views.new_list,name='new_list'),
    url(r'^(\d+)/$',views.view_list,name='view_list'),
    url(r'^(\d+)/add_item$',views.add_item,name='add_item')
]
#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 1:26
# @Author   : guanqiao
# TODO(guanqiao):
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('home/', views.home),
    path('login/', views.login),
    path('showhome/', views.showhome),
    path('quit/', views.quit),
]

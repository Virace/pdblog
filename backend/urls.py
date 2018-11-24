#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 14:59
# @Author  : Virace
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from backend import views

urlpatterns = [
    url(r'^users/', views.Users.as_view({'get': 'list', 'post': 'create'})),
]


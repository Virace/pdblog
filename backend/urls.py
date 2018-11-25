#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 14:59
# @Author  : Virace
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from backend import views

urlpatterns = [
    url(r'^users/$', views.UsersActionViews.as_view({'get': 'list', 'post': 'create'})),
    url(r'^users/(?P<pk>\d+)$', views.UsersActionViews.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'})),
    url(r'^auth/$', views.AuthViews.as_view()),
]


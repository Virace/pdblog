#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 23:15
# @Author  : Virace
# @File    : Permission.py
# @Software: PyCharm

from rest_framework import permissions

from backend import models


class UserActionPermission(permissions.BasePermission):

    message = '权限不足'

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if not request.user:
            return False
        obj = models.Usermeta.objects.filter(uid=request.user, key='type').first()
        if not obj:
            return False
        if obj.value != '0':
            return False

        return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

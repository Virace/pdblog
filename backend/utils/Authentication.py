#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 23:56
# @Author  : Virace
# @File    : Authentication.py
# @Software: PyCharm

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework import request
from backend import models
from backend.utils import Token


class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()

        if not token_obj:
            raise exceptions.AuthenticationFailed('用户验证失败')

        tk = Token.UserAuthToken()
        flag = tk.certify(key=token_obj.user.login, token=token_obj.token)
        if not flag:
            raise exceptions.AuthenticationFailed('用户验证信息过期')
        return token_obj.user, token_obj

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        pass

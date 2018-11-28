#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 15:05
# @Author  : Virace
# @File    : Serializer.py
# @Software: PyCharm

from rest_framework import serializers
from backend import models


class UserInfoSerializers(serializers.ModelSerializer):
    # registered = serializers.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    # status = serializers.IntegerField(verbose_name='账户状态', default=0)
    status = serializers.IntegerField(source='get_status_display')

    class Meta:
        model = models.Users
        fields = ('login', 'nickname', 'email', 'url', 'registered', 'status')
        read_only_fields = ('registered', 'status', )
        # exclude = ('registered', 'status', )


class UserTokenSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.UserToken
        fields = '__all__'

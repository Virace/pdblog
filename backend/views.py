from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.versioning import QueryParameterVersioning


from backend import models
from backend.utils import Serializer, Authentication


class UsersActionViews(ModelViewSet):
    authentication_classes = (Authentication.UserAuthentication,)
    # 过滤ststus=删除的用户
    queryset = models.Users.objects.exclude(status=9)
    serializer_class = Serializer.UserSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # 假删除
        instance.status = 9
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthViews(APIView):
    @classmethod
    def post(cls, request, *args, **kwargs):
        username = request.data.get('login')
        password = request.data.get('passw')
        obj = models.Users.objects.filter(login=username, passw=password).first()
        print(username, password)
        return Response('1')

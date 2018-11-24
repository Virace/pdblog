from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from backend import models
from backend.utils import Serializer


class Users(mixins.CreateModelMixin, GenericViewSet):
    queryset = models.Users.objects.all()
    serializer_class = Serializer.UserSerializers

    def list(self, requests, *args, **kwargs):
        users = self.get_queryset()
        ser = self.get_serializer(instance=users, many=True)
        return Response(ser.data)

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)
        return Response('1')

    def delete(self, requests, *args, **kwargs):
        pass

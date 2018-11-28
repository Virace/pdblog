from django.shortcuts import render

# Create your views here.

from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.versioning import QueryParameterVersioning


from backend import models
from backend.utils import Authentication, Serializer, Token, Permission


class UsersActionViews(viewsets.ModelViewSet):
    authentication_classes = (Authentication.UserAuthentication,)
    # 过滤ststus=删除的用户
    permission_classes = (Permission.UserActionPermission, )
    queryset = models.Users.objects.exclude(status=9)
    serializer_class = Serializer.UserInfoSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # 假删除
        instance.status = 9
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAuthViews(views.APIView):

    def post(self, request, *args, **kwargs):
        """
        用户登录
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        username = request.data.get('login')
        password = request.data.get('passw')
        obj = models.Users.objects.exclude(status=9).filter(login=username, passw=password).first()
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)

        tk = Token.UserAuthToken()
        str_token = tk.get(obj.login)
        this_tk = models.UserToken.objects.create(user=obj, token=str_token)

        ser = Serializer.UserTokenSerializers(instance=this_tk)

        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        """
        用户注销
        :param request:
        :param args:
        :param kwargs:
        :return:
        """


        pass

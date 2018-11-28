from django.db import models

# Create your models here.


class Users(models.Model):
    status_list = (
        ('0', '正常'),
        ('1', '封禁'),
        ('9', '删除')
    )
    login = models.CharField(verbose_name='用户名', max_length=15, unique=True, null=False)
    passw = models.CharField(verbose_name='密码', max_length=30, null=False)
    nickname = models.CharField(verbose_name='昵称', max_length=15, unique=True)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    url = models.URLField(verbose_name='网址', null=True)
    registered = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    status = models.IntegerField(verbose_name='账户状态', choices=status_list, default=0)


class UserToken(models.Model):
    user = models.OneToOneField(to=Users)
    token = models.CharField(verbose_name='密码', max_length=30, null=True)


class Usermeta(models.Model):
    uid = models.OneToOneField(verbose_name='用户', to=UserToken)
    key = models.CharField(verbose_name='key', unique=True, max_length=20)
    value = models.CharField(verbose_name='value', max_length=20)


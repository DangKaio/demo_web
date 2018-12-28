from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """必须要继承models.Model类，固定写法"""
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
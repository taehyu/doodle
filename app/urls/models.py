from uuid import uuid4
from django.db import models


class Url(models.Model):
    url = models.URLField(default='www.google.com')


class Parent(models.Model):
    uuid = models.UUIDField(default=uuid4())


class Child(models.Model):
    uuid = models.UUIDField(default=uuid4())
    parent = models.ForeignKey('urls.Parent', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

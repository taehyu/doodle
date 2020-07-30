import time

from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import Users
from users.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        * users/6/ 에 접근 시 캐시를 생성, 이후에 캐시 기간이 만료되기 전 까지는 캐시를 불러온다.
        request: url <users_pk:> 동적인 키를 생성
        udpate, delete 시에는 기존에 존재하는 캐시를 삭제
        :return:
        """
        # instance = self.get_object()
        # serializer = self.get_serializer(instance)
        # return Response(serializer.data)

        # key = f"url{kwargs['pk']}"
        key = f"user{self.kwargs['pk']}"
        instance = cache.get(key)
        if instance is None:
            instance = self.get_object()
            cache.set(key, instance, 60)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)








import time

from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
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
        update, delete 시에는 기존에 존재하는 캐시를 삭제
        :return:
        """
        # instance = self.get_object()
        # serializer = self.get_serializer(instance)
        # return Response(serializer.data)
        key = f"user{self.kwargs['pk']}"
        instance = cache.get(key)
        # print(0/0)
        if instance is None:
            instance = self.get_object()
            cache.set(key, instance, 60)
        serializer = self.get_serializer(instance)
        # return Response(serializer.data)
        return Response(0 / 0)

    # def retrieve(self, request, *args, **kwargs):
    #     key = kwargs['pk']
    #     instance = cache.get(key)
    #     if not instance:
    #         time.sleep(3)
    #         instance = self.get_object()
    #         cache.set(key, instance, 3)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


class DoodleViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        data = {"key": "value"}
        return Response(data['key'])

    @action(methods=["POST"], detail=False)
    def test(self, request):
        self.check(0, 1, c=2)

    def check(self, request, *args, **kwargs):
        a = 100
        b = 'abc'
        c = {'key': 'val'}

        return a/b

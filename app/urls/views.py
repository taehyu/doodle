from datetime import datetime
from time import sleep

from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
#
#
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from urls.models import Url
from urls.serializers import UrlSerializer


class UrlViewSet(ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(methods=['GET'], detail=False)
    def cache_test(self, request):
        key = 'my_key'
        val = cache.get('KEY')
        if not val:
            sleep(2)
            val = 'fast-campus'
            cache.set('KEY', val, 60*60)

        data = {
            'my_data': val,
            'extra': datetime.now(), #실시간으로 cache안함
        }
        return Response(data=data)

    # from URLViewSet(viewsets.ModelViewSet):
    #     queryset = models.URL.objects.all()
    #
    #     def get_queryset(self):
    #         qs = super().get_queryset()
    #
    #         if self.action == 'list':
    #             qs = qs.select_related('parent', 'user')
    #             as = qs.prefetch_related('img')
    #         return qs

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from short.models import Short
from short.serializers import ShortSerializer


class ShortViewSet(viewsets.ModelViewSet):
    queryset = Short.objects.all()
    serializer_class = ShortSerializer

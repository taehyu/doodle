from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from djoser.views import UserViewSet
from rest_framework import serializers
from django.core.cache import cache
from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name',)


from rest_framework import serializers

from urls import models


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Url
        fields = ('id',)
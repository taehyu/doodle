from rest_framework import serializers
from .models import Urls


class UrlSerializer(serializers.ModelSerializer):
    counting = serializers.ReadOnlyField()
    changeurl = serializers.ReadOnlyField()

    class Meta:
        model = Urls
        fields = (
            'id',
            'url',
            'counting',
            'changeurl',
        )

from rest_framework.serializers import ModelSerializer
from urlshort.models import UrlShort


class ShortenerSerializer(ModelSerializer):
    class Meta:
        model = UrlShort
        fields = ('url_bf', 'url_af','count',)
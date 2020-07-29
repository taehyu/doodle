from rest_framework import serializers

from short.models import Short


class ShortSerializer(serializers.ModelSerializer):
    output_url = serializers.ReadOnlyField()

    class Meta:
        model = Short
        fields = ('id', 'input_url', 'output_url')




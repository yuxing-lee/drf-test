from rest_framework import serializers

from .models import ImageInfo


class ImageInfoSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = ImageInfo
        fields = ['id', 'image_url', 'create_at']

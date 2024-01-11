from rest_framework import serializers

from .models import ImageInfo


class ImageInfoSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = ImageInfo
        fields = ['id', 'image_url', 'create_at']


class ImageProcessSerializer(serializers.Serializer):
    image_url = serializers.CharField(allow_blank=True, allow_null=True)
    function = serializers.CharField(allow_blank=True)
    params = serializers.JSONField()
    changed = serializers.BooleanField()
    child = serializers.ListField(child=serializers.JSONField(), allow_empty=True, required=False)

    def to_representation(self, instance):
        return super(ImageProcessSerializer, self).to_representation(instance)

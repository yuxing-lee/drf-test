from rest_framework import mixins, viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from .models import ImageInfo
from .serializers import ImageInfoSerializer


class ImageInfoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ImageInfo.objects.order_by('-create_at')
    serializer_class = ImageInfoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

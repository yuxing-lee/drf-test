from rest_framework import mixins, status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import ImageInfo
from .serializers import ImageInfoSerializer, ImageProcessSerializer


class ImageInfoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ImageInfo.objects.order_by('-create_at')
    serializer_class = ImageInfoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()


class ImageProcessViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ImageProcessSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

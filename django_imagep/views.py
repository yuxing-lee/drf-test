import os

from rest_framework import mixins, status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import ImageInfo
from .serializers import ImageInfoSerializer, ImageProcessSerializer
from .utils import imageProcess


class ImageInfoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ImageInfo.objects.order_by('-create_at')
    serializer_class = ImageInfoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()
        # delete old image
        image_url = serializer.data["image_url"]
        filename = image_url.split('/')[-1]
        media_index = image_url.index("media/")
        filename_index = image_url.index(filename)
        image_path = image_url[media_index:filename_index]
        for file in os.listdir(image_path):
            if file != filename:
                os.remove(image_path + file)


class ImageProcessViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ImageProcessSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = imageProcess(None, serializer.data)
        return Response(data, status=status.HTTP_200_OK)

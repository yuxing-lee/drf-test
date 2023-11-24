from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import Query
from .serializers import GoogleTranslateSerializer


class TranslateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Query.objects.all()
    serializer_class = GoogleTranslateSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.translate()
        serializer.save()
        return Response(result, status=status.HTTP_201_CREATED)

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Translate
from .serializers import TranslateSerializer


class TranslateViewSet(viewsets.GenericViewSet):
    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer

    def list(self, request):
        translate_query = self.get_queryset()
        return Response(self.get_serializer(translate_query, many=True).data)

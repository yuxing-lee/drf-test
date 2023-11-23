from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import Query
from .serializers import QuerySerializer
from .utils import translate_text


class TranslateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def create(self, request):
        translate_result = translate_text(request.data["source_text"],
                                          request.data["target_language"])
        serializer = self.serializer_class(data=translate_result)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

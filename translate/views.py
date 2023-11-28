from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import Query
from .serializers import QuerySerializer
from .services import GoogleTranslateService


class TranslateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        source_text = serializer.validated_data.get("source_text")
        source_language = serializer.validated_data.get("source_language")
        target_language = serializer.validated_data.get("target_language")
        target_text, source_language = GoogleTranslateService().translate(
            source_text, target_language, source_language)
        translate = self.get_queryset().filter(source_text=source_text,
                                               target_language=target_language,
                                               source_language=source_language).first()
        if translate:
            serializer = QuerySerializer(translate)
        else:
            serializer.validated_data["target_text"] = target_text
            serializer.validated_data["source_language"] = source_language
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

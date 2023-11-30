from django.contrib.auth import get_user_model
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .filters import TranslateFilter
from .models import Query, Translate
from .serializers import QuerySerializer, TranslateSerializer
from .services import GoogleTranslateService

User = get_user_model()


class QueryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
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
        query = self.get_queryset().filter(source_text=source_text,
                                           target_language=target_language,
                                           source_language=source_language).first()
        if query:
            serializer = QuerySerializer(query)
        else:
            serializer.validated_data["target_text"] = target_text
            serializer.validated_data["source_language"] = source_language
            serializer.save()
        # save translation by user
        translate_log = TranslateSerializer(data={
            "query_id": serializer.instance.id,
            "user": request.user.id
        })
        translate_log.is_valid(raise_exception=True)
        translate_log.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TranslateViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer
    filterset_class = TranslateFilter

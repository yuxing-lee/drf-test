from google.cloud import translate_v2 as translate
from rest_framework import serializers

from .models import Query


class QuerySerializer(serializers.ModelSerializer):
    target_text = serializers.CharField(required=False)
    source_language = serializers.CharField(required=False)

    class Meta:
        model = Query
        fields = '__all__'


class GoogleTranslateSerializer(QuerySerializer):

    translate_client = translate.Client()
    supported_languages = [lang["language"] for lang in translate_client.get_languages()]

    def translate(self):
        source_text = self.validated_data.get('source_text')
        source_language = self.validated_data.get('source_language')
        target_language = self.validated_data.get('target_language')
        if target_language not in self.supported_languages:
            raise ValueError("Target language not supported")
        if source_language and source_language not in self.supported_languages:
            raise ValueError("Source language not supported")
        result = self.translate_client.translate(source_text,
                                                 target_language=target_language,
                                                 source_language=source_language)
        self.validated_data["target_text"] = result["translatedText"]
        if "detectedSourceLanguage" in result:
            self.validated_data["source_language"] = result["detectedSourceLanguage"]
        return self.validated_data

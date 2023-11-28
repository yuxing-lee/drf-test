from rest_framework import serializers

from .models import Query, Translate


class QuerySerializer(serializers.ModelSerializer):
    target_text = serializers.CharField(required=False)
    source_language = serializers.CharField(required=False)

    class Meta:
        model = Query
        fields = '__all__'


class TranslateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translate
        fields = '__all__'

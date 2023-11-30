from rest_framework import serializers

from .models import Query, Translate


class QuerySerializer(serializers.ModelSerializer):
    target_text = serializers.CharField(required=False)
    source_language = serializers.CharField(required=False)

    class Meta:
        model = Query
        fields = '__all__'


class TranslateSerializer(serializers.ModelSerializer):
    query_count = serializers.SerializerMethodField()

    def get_query_count(self, obj):
        return Translate.objects.filter(user=obj.user, query_id=obj.query_id.id).count()

    class Meta:
        model = Translate
        fields = '__all__'

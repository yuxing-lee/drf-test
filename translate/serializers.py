from rest_framework import serializers

from .models import Query


class QuerySerializer(serializers.ModelSerializer):
    target_text = serializers.CharField(required=False)
    source_language = serializers.CharField(required=False)

    class Meta:
        model = Query
        fields = '__all__'

import django_filters
from django_filters import rest_framework as filters

from .models import Translate


class TranslateFilter(filters.FilterSet):
    query_date_gte = django_filters.DateFilter(field_name="created_at", lookup_expr='gte')
    query_date_lte = django_filters.DateFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Translate
        fields = ['query_id', 'query_date_gte', 'query_date_lte']

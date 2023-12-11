from django.contrib import admin

from .models import Query, Translate


@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    list_display = ['user', 'query_id', 'created_at']


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ['source_text', 'target_text', 'source_language', 'target_language']

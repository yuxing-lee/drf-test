from django.contrib import admin

from .models import Translate


@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    list_display = ['user', 'query', 'created_at']

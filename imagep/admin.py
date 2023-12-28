from django.contrib import admin

from .models import ImageInfo


@admin.register(ImageInfo)
class TranslateAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_url', 'create_at']

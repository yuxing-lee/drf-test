from django.conf import settings
from django.db import models


class Query(models.Model):
    source_text = models.TextField()
    target_text = models.TextField()
    source_language = models.CharField(max_length=10)
    target_language = models.CharField(max_length=10)


class Translate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    query_id = models.ForeignKey(Query, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

from django.conf import settings
from django.db import models


class Translate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models

from .utils import upload_to


class ImageInfo(models.Model):
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

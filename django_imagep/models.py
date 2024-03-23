from django.db import models

from .utils import uploadTo


class ImageInfo(models.Model):
    image_url = models.ImageField(upload_to=uploadTo, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.conf import settings
from chunked_upload.models import AbstractChunkedUpload


class MyChunkedUpload(AbstractChunkedUpload):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chunked_uploads', null=True)

from django.conf import settings
from django.db import models


class StoredPassword(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False
    )
    password = models.CharField(
        'Password hash',
        max_length=255,
        editable=False
    )
    date = models.DateTimeField(
        'Date',
        auto_now_add=True,
        editable=False
    )


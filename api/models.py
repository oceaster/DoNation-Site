from django.db import models
from django.utils import timezone

class Pledge(models.Model):

    class Meta:
        ordering = ['-id']

    uid = models.TextField(
        null=False, blank=False, editable=False
    )
    pledge = models.TextField(
        null=False, blank=False
    )
    save_co2 = models.FloatField(
        null=False, blank=False, default=0.0
    )
    timestamp = models.DateTimeField(
        null=False, default=timezone.now, editable=False
    )

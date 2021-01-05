from django.db import models
import uuid

class DataEntery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    infected = models.PositiveIntegerField( null=True, blank=False)
    infectedDate = models.DateField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Data Enteries"
        ordering = ['created']

    def __str__(self):
        return f'The number of infected are ({self.infected}) on ({self.infectedDate})'

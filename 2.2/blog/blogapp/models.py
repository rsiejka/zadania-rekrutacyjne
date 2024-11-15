import uuid
from django.conf import settings
from django.db import models

# Create your models here.

class Entry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    creatorId = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    addedDate = models.DateField(blank=False, null=False)
    content = models.CharField(max_length=500)

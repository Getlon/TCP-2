from django.db import models
from django.utils import timezone


class Contributor(models.Model):
    full_name = models.TextField()
    donated_amount = models.BigIntegerField()


class Event(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="app1/static/images/")
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

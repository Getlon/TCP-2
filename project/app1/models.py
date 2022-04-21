from django.db import models


class Contributor(models.Model):
    full_name = models.TextField()
    donated_amount = models.BigIntegerField()

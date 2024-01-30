from django.db import models


class DisplayData(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

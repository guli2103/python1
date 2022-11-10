from django.db import models

class Odam(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    yosh = models.IntegerField(default=16)

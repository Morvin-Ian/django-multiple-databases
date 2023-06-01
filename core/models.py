from django.db import models

class Core(models.Model):
    name = models.CharField(max_length=250)
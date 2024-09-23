from django.db import models

class Perpustakaan(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
# Create your models here.

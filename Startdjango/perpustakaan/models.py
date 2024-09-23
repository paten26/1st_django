from django.db import models

class Perpustakaan(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    penulis = models.CharField(max_length=200, default="NA")
    stok = models.IntegerField(default=1)
# Create your models here.

from django.db import models

# Create your models here.
class administrasi(models.Model):
    judul = models.CharField(max_length=40)
    pasien = models. CharField(max_length=40)

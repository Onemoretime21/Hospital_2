from django.conf import settings
from django.db import models


class Hospitals(models.Model):
    hospital = models.CharField(max_length=200)
    main_doctor = models.CharField(max_length=200)
    hirurg = models.CharField(max_length=200, null=True, blank=True, default='')
    terapevt = models.CharField(max_length=200, null=True, blank=True, default='')
    medsestra = models.CharField(max_length=200)
    pasienty = models.CharField(max_length=200)


    def __str__(self):
        return self.hospital

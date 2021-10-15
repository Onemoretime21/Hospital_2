from django.conf import settings
from django.db import models

<<<<<<< HEAD
class Hospitals(models.Model):
    hospital = models.CharField(max_length=200)
    main_doctor = models.CharField(max_length=200)
    hirurg = models.CharField(max_length=200)
    terapevt = models.CharField(max_length=200)
    medsestra = models.CharField(max_length=200)
    pasienty = models.CharField(max_length=200)


    def __str__(self):
        return self.hospital
=======
# Create your models here.

class LatestNews(models.Model):
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
>>>>>>> 4a9444ef282364627b79fc5e00fabf5dd8e41f12

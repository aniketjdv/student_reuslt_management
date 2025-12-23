from django.db import models
from django.utils import timezone
# Create your models here.
class Studentdemo(models.Model):
    STYPE = [('IT','Information Technology'),
             ('CS','Computer Science'),
             ('MBA','Buisness Admstration')
             ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3,choices=STYPE)

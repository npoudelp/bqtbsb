from django.db import models
from django.utils import timezone

# Create your models here.

class upload_files(models.Model):
    file_path = models.CharField(max_length=100, null=False, blank=False)
    upload_date = models.DateField(default=timezone.now())

    


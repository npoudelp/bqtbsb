from django.db import models
from django.utils import timezone

# Create your models here.

class upload_files(models.Model):
    FILE_STATUS_CODE = [('Red'), ('Yellow'), ('Green')]
    file_path = models.CharField(max_length=100, null=False, blank=False)
    upload_date = models.DateField(default=timezone.now(), blank=True, null=False)
    file_status = models.CharField(choices=FILE_STATUS_CODE, max_length=20, null=False, blank=False)
    is_shared = models.BooleanField(default=False)
    


    


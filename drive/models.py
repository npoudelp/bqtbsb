from django.db import models
from django.utils import timezone

# Create your models here.

class upload_files(models.Model):
    FILE_STATUS_CODE = [
        ('0', 'Red'),
        ('1', 'Yellow'),
        ('2', 'Green'),
    ]
    file_path = models.ImageField(null=False, blank=False, upload_to='drive_images/')
    upload_date = models.DateField(default=timezone.now(), blank=True, null=False)
    file_status = models.CharField(choices=FILE_STATUS_CODE, max_length=20, null=False, blank=False, default="Red")
    is_shared = models.BooleanField(default=False)
    
    def __str__(self):
        return self.file_path


    


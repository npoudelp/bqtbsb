from django.db import models
from django.utils import timezone

# Create your models here.

class tags(models.Model):
    tag_name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.tag_name


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
    image_tag = models.ForeignKey(tags, on_delete=models.PROTECT, null=False, blank=True, default="Null")
    
    def __str__(self):
        return self.file_path


    


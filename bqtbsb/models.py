from django.db import models
from django.utils import timezone


class my_profile(models.Model):
    user_name = models.CharField(max_length=30, blank=False, null=False)
    last_update = models.DateField(default=timezone.now(), blank=True, null=False)
    user_email = models.EmailField(null=False, blank=False)
    user_image = models.ImageField(null=False, blank=False, upload_to='user_profile_image')
    user_address = models.CharField(null=False, blank=False, max_length=40)
    user_phone = models.CharField(null=False, blank=False, max_length=15)
    user_user = models.CharField(null=False, blank=True, max_length=50)

    def __str__(self):
        return self.user_name
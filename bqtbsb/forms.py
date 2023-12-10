from django import forms
from bqtbsb.models import my_profile


class my_profile_form(forms.ModelForm):
    class Meta:
        model = my_profile
        fields = ['user_name', 'user_address', 'user_phone', 'user_email', 'user_image']
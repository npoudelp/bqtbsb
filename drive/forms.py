from django import forms
from drive.models import upload_files

class upload_files_form(forms.ModelForm):
    class Meta:
        model = upload_files
        fields = ['file_path', 'file_status']
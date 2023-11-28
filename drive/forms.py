from django import forms
from drive.models import upload_files, tags

class upload_files_form(forms.ModelForm):
    class Meta:
        model = upload_files
        fields = ['file_path', 'file_status', 'image_tag']


class tags_form(forms.ModelForm):
    class Meta:
        model = tags
        fields = ['tag_name']
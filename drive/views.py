from django.shortcuts import render, redirect
from drive.forms import upload_files_form
from django.contrib import messages
from django.contrib.auth import decorators
from drive.models import upload_files as drive_image
from django.http import Http404

def my_drive(request):


    res = {
        "upload_form": upload_files_form,
        "images": drive_image.objects.all().order_by('-id')
    }

    if request.method == 'POST':
        form_data = upload_files_form(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Image added to drive...")
        else:
            messages.error(request, "Error adding image...")

    return render(request, "drive/drive.html", res)


def delete_file(request, id):
    res = {}
    try:
        file = drive_image.objects.get(id=id)
        if file.delete():
            messages.success(request, "Image deleted...")
            return redirect('drive:my_drive')
        else:
            messages.error(request, "Error deleting image...")
            return redirect('drive:my_drive')
    except drive_image.DoesNotExist:
        messages.error(request, "Image does not exist...")
        raise(Http404)

    return render(request, "drive/drive.html", res)
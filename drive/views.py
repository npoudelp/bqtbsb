from django.shortcuts import render, redirect
from drive.forms import upload_files_form, tags_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from drive.models import upload_files as drive_image, tags
from django.http import Http404
from os import remove


def get_from_tags():
    data = tags.objects.all().order_by('-id')
    return data


@login_required(login_url='login')
def my_drive(request):
    res = {
        "upload_form": upload_files_form,
        "images": drive_image.objects.all().order_by('-id'),
        'tags': get_from_tags(),
        'add_tag_form': tags_form,
    }

    if request.method == 'POST':
        form_data = upload_files_form(request.POST, request.FILES)
        tags_data = tags_form(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Image added to drive...")
        elif tags_data.is_valid():
            tags_data.save()
            messages.success(request, "Tag added...")
        else:
            messages.error(request, "Error performing task...")

    return render(request, "drive/drive.html", res)


@login_required(login_url='login')
def delete_file(request, id):
    res = {}
    try:
        file = drive_image.objects.get(id=id)
        if file.delete():
            remove(f'media/{file.file_path.url}')
            messages.success(request, "Image deleted successfully...")
            return redirect('drive:my_drive')
        else:
            messages.error(request, "Error deleting image...")
            return redirect('drive:my_drive')
    except drive_image.DoesNotExist:
        messages.error(request, "Image does not exist...")
        return redirect('drive:my_drive')


@login_required(login_url='login')
def filter_file(request, key):
    if key == 'old_first':
        data = drive_image.objects.all()
    elif key == 'new_first':
        data = drive_image.objects.all().order_by('-id')
    elif key == 'restricted':
        data = drive_image.objects.all().filter(file_status='0')
    elif key == 'strict':
        data = drive_image.objects.all().filter(file_status='1')
    elif key == 'unrestricted':
        data = drive_image.objects.all().filter(file_status='2')
    else:
        tag_id = tags.objects.values_list('id', flat=True).filter(tag_name=key)
        data = drive_image.objects.filter(image_tag__in=tag_id)
    res = {
        "upload_form": upload_files_form,
        'images': data,
        'tags': get_from_tags(),
        'add_tag_form': tags_form,
    }

    if request.method == 'POST':
        form_data = upload_files_form(request.POST, request.FILES)
        tags_data = tags_form(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Image added to drive...")
        elif tags_data.is_valid():
            tags_data.save()
            messages.success(request, "Tag added...")
        else:
            messages.error(request, "Error performing task...")

    return render(request, "drive/drive.html", res)


@login_required(login_url='login')
def file_viewer(request, id):
    if request.method == 'POST':
            form_data = upload_files_form(request.POST, request.FILES)
            tags_data = tags_form(request.POST)
            if form_data.is_valid():
                form_data.save()
                messages.success(request, "Image added to drive...")
            elif tags_data.is_valid():
                tags_data.save()
                messages.success(request, "Tag added...")
            else:
                messages.error(request, "Error performing task...")

    try:
        file = drive_image.objects.get(id=id)
                
    except drive_image.DoesNotExist:
        messages.error(request, "Image does not exist...")
        raise(Http404)

    res = {
        "upload_form": upload_files_form,
        'tags': get_from_tags(),
        'add_tag_form': tags_form,
        'image': file,
    }
    return render(request, "drive/file_viewer.html", res)
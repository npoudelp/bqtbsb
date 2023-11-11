from django.shortcuts import render, redirect

def dashboard(request):
    res = {}
    return render(request, "drive/dashboard.html", res)

def my_drive(request):
    res = {}
    return render(request, "drive/drive.html", res)

def upload_file(request):
    return render(request, "dashboard.html")
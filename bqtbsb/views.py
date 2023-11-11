from django.shortcuts import render

def dashboard(request):
    res = {}
    return render(request, "dashboard.html", res)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    res = {}
    return render(request, "dashboard.html", res)


def login(request):
    res = {}
    return render(request, 'login.html', res)
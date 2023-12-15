from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from bqtbsb.models import my_profile as profile
from bqtbsb.forms import my_profile_form


@login_required(login_url='login')
def dashboard(request):
    res = {}
    return render(request, "dashboard.html", res)


def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        user_auth = authenticate(request, username=uname, password=passwd)

        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, f"Welcome, {user_auth}")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid login data...")

    res = {}
    return render(request, 'login.html', res)


@login_required(login_url='login')
def user_logout(request):
    res = {}
    logout(request)
    messages.success(request, "Thank You for your visit...")
    return render(request, 'login.html', res)


@login_required(login_url='login')
def my_profile(request):

    profile_data = profile.objects.all()

    res = {
        'profile':profile_data,
        'profile_update_form': my_profile_form()
    }
    return render(request, 'my_profile.html', res)
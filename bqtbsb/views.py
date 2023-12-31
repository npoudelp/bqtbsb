from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from bqtbsb.models import my_profile as profile
from bqtbsb.forms import my_profile_form
from django.http import Http404


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
            try:
                request.session['profile_image'] = profile.objects.get(user_user=user_auth).user_image.url
            except profile.DoesNotExist:
                profile_image = None
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

    update = True
    try:
        data = profile.objects.get(user_user=request.user.username)
        update_form = my_profile_form(instance=data)

    except profile.DoesNotExist:
        update = False
        data = None
        update_form = my_profile_form

    if request.method == 'POST':
        update_profile_data = my_profile_form(request.POST, request.FILES, instance=data)
        add_profile = my_profile_form(request.POST, request.FILES)
        if update_profile_data.is_valid() and update == True:
            if update_profile_data.save():
                messages.success(request, "Profile updated...")
            else:
                messages.error(request, "Error updating profile...")
        
        if add_profile.is_valid() and update == False:
            hold = add_profile.save(commit=False)
            hold.user_user = request.user.username
            hold.save()

        else:
            pass

    res = {
        'profile':data,
        'profile_update_form': update_form,
    }
    return render(request, 'my_profile.html', res)

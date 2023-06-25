from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from .form import SignupForm, EditProfileForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'members/login_or_signup.html', {'title': 'Login', 'form': form})


def profile_view(request):
    return render(request, 'members/profile.html', {'title': 'Profile'})


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()

    return render(request, 'members/login_or_signup.html', {'title': 'Signup', 'form': form})


@login_required()
def profile_view(request):
    return render(request, 'members/profile.html', {'title': 'Profile'})


@login_required()
def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'members/login_or_signup.html', {'title': 'Signup', 'form': form})


@login_required()
def logout_view(request):
    logout(request)
    return redirect('index')

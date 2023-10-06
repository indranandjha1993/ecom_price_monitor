from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/profile.html')


def edit_profile(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.id != user_id:
        return redirect('home')  # or some other appropriate response

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


def change_password(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.id != user_id:
        return redirect('home')  # or some other appropriate response

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # maybe add a success message here
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:  # If user is already logged in
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redirect to home after login
    return render(request, 'accounts/login.html')


def register(request):
    if request.user.is_authenticated:  # If user is already logged in
        return redirect('home')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')  # redirect to home after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    if not request.user.is_authenticated:  # If user is not logged in
        return redirect('login')
    return render(request, 'accounts/home.html')

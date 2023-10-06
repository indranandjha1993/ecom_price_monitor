from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm


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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import forms


def create_smartphone(request):
    if request.method == 'POST':
        form = forms.SmartphoneForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.SmartphoneForm()

    return render(request, 'www/create_form.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = forms.CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.is_staff()
            # user.save()

    form = forms.CustomUserForm()
    return render(request, 'www/sign_up.html', {'form':form})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)

    return render(request, 'www/sign_in.html')
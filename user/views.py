from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from user.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.urls import reverse
from user.models import User


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context: dict[str, str] = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'login.html', context)


def registration(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserRegistrationForm()
    context: dict[str, str] = {
        'title': 'Home - Регистрация',
        'form': form,
    }
    return render(request, 'registration.html', context)


def profile(request):
    user = User.objects.filter(username=request.user.username)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        print(form)
        if form.is_valid():
            if form.cleaned_data['username']:
                user.update(username=form.cleaned_data['username'])
            if form.cleaned_data['email']:
                user.update(email=form.cleaned_data['email'])
            if form.cleaned_data['country']:
                user.update(country=form.cleaned_data['country'])
            if form.cleaned_data['first_name']:
                user.update(first_name=form.cleaned_data['first_name'])
            if form.cleaned_data['last_name']:
                user.update(last_name=form.cleaned_data['last_name'])
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = ProfileForm()
    profile = [{
        "username": user[0].username,
        "email": user[0].email,
        "country": user[0].country,
        "data_joined": user[0].date_joined,
        "first_name": user[0].first_name,
        "last_name": user[0].last_name,
    }]
    return render(request, 'profile.html', context={'profile': profile[0], 'form': form})


def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))

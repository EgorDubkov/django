from django.shortcuts import render
from django.contrib import auth
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    title = 'входа'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'регистрация'

    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()

        return HttpResponseRedirect(reverse('auth:register'))
    else:
        register_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'register_form': register_form,
    }
    return render(request, 'authapp/login.html', context)


def edit(request):
    title = 'профиль'

    if request.method == "POST":
        edit_form = ShopUserEditForm(request.POST, request.FILES, isinstance=request.user)
        if edit_form.is_valid():
            edit_form.save()

        return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(isinstance=request.user)

    context = {
        'title': title,
        'edit_form': edit_form,
    }
    return render(request, 'authapp/edit.html', context)
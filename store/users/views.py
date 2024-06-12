from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, PasswordEmailForm
from products.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    form = UserProfileForm(instance=request.user)
    context = {'title': 'Салон проката', 'form': form}
    return render(request, 'users/profile.html', context)


class WebPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_email.html'


# class WebPasswordResetDone(PasswordResetDoneView):
#     template_name = 'users/password_reset_success.html'

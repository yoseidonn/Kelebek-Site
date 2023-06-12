from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from .forms import LoginForm, RegisterForm


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    messages.info(request, "Maalesef bu hesap aktif değil.")
            else:
                messages.info(request, "Kullanıcı adı ve parolanızı kontrol ediniz.")
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {"form": form})


def user_register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hesabınız başarıyla oluşturulmuştur. Oturum açabilirsiniz.")
            return HttpResponseRedirect("/accounts/login")

    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


@login_required(login_url='/accounts/login')
def user_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "test.html")


def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect("/")
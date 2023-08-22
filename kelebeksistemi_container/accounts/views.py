from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.cache import cache
from django.shortcuts import render, redirect

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from django.conf import settings
from accounts.forms import LoginForm, RegisterForm, EditForm
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import CustomUser
from accounts.tokens import account_activation_token_generator
from program.models import Purchase, LicenseKey

import os, json, dotenv
dotenv.load_dotenv()


def send_activation_email(request: HttpResponse, user: CustomUser):
    subject = "E-Posta adresinizi onaylayın!"
    message = render_to_string("accounts/email.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.password)),
        'token': account_activation_token_generator.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    
    try:
        send_mail(subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
        )
        messages.success(request, "E-Posta adresinize bir doğrulama postası gönderildi! Not: Spam klasörünü kontrol etmeyi unutmayın.")

    except Exception as e:
        messages.info(request, "Mesaj gönderilirken bir hata meydana geldi, lütfen internet bağlantınızı kontrol edin!")
        raise e

    
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

    context = {"form": form}
    
    return render(request, "accounts/login.html", context)


def user_register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = CustomUser.objects.all().filter(email=email)
            if users:
                messages.info(request, "Bu e-posta adresi kullanılıyor.")
            else:
                form.save()
                messages.success(request, "Hesabınız başarıyla oluşturulmuştur. Oturum açabilirsiniz.")
                return HttpResponseRedirect("/accounts/login")
        else:
            messages.info(request, "Formunuzda bir şeyler yanlış. Lütfen yeniden deneyiniz.")
    else:
        form = RegisterForm()

    context = {"form": form}
    
    return render(request, "accounts/register.html", context)


@login_required(login_url='/accounts/login')
def user_profile(request: HttpRequest) -> HttpResponse:
    user = request.user
    if request.method == "POST":
        send_activation_email(request, user)

    purchase_objects = Purchase.objects.filter(user=user).order_by("-purchase_date")   
    license_keys = list()
    for purchase in purchase_objects:
        license_keys.append(LicenseKey.objects.get(purchase=purchase))
    
    purchases = zip(purchase_objects, license_keys)
    
    context = {"purchases": purchases}
    
    return render(request, "accounts/profile.html", context)


def user_edit_profile(request: HttpRequest) -> HttpResponse:
    user = request.user
    email = user.email
    if request.method == "POST":
        form = EditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            try:
                profile_photo = form.cleaned_data['profile_photo']
                request.user.profile_photo = profile_photo
                
                new_email = form.cleaned_data['email']
                if new_email != email:
                    user.is_email_verified = 'Nonverified'
                    
                request.user.save()
                messages.success(request, "Profil bilgileriniz başarıyla değiştirilmiştir.")
                return redirect('profile')

            except ValidationError:
                # Handle validation error for the uploaded file if needed
                messages.info(request, "Dosya yüklenirken bir hata meydana geldi.")
        else:
            messages.info(request, "Formunuzda bir şeyler ters gitti. Lütfen tekrar deneyiniz.")
    else:
        form = EditForm(instance=user)

    return render(request, "accounts/edit_profile.html", context={"form": form})


def user_verify_email(request: HttpRequest, uid: str, token: str) -> HttpResponse:
    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = CustomUser.objects.get(password=uid)
    except:
        user = None
            
    if (user is None) or (not account_activation_token_generator.check_token(user, token)):
        messages.info(request, "Parola sıfırlama bağlantısı geçersiz!")
        return HttpResponseRedirect("/")
    
    if request.method == "POST":
        if (user is not None) and (account_activation_token_generator.check_token(user, token)):
            user.is_email_verified = 'Verified'
            user.save()

            messages.success(request, "E-Postanızı doğruladığınız için teşekkür ederiz. Keyifli ziyaretler!")
            return HttpResponseRedirect("/")
    
    return render(request, 'accounts/verify_email.html')
    

def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect("/")
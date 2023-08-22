from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from pages.models import Feature, Heading
from accounts.models import CustomUser


# Create your views here.
def team(request: HttpRequest) -> HttpResponse:
    users = CustomUser.objects.filter(role='Developer')
    users = enumerate(users)

    context = {"users": users}
    
    return render(request, "about/team.html", context)

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.info(request, "Mesajınız başarıyla gönderildi. En yakın zamanda size dönüş yapacağız.")
            form.save()
            return HttpResponseRedirect("/about/contact")
        else:
            messages.info(request, "Formunuz geçersiz.")
    else:
        form = ContactForm()
    
    context = {"form": form}
    
    return render(request, "about/contact.html", context)

def privacy_terms(request: HttpRequest) -> HttpResponse:
    return render(request, "about/privacy_terms.html")
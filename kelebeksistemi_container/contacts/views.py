from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import ContactForm


# Create your views here.
def contact(request: HttpRequest) -> HttpResponse:
    form = ContactForm()
    return render(request, "contact.html", {"form": form})
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
#from .forms import RegisterForm


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")
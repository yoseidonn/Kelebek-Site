from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.
def purchase_options(request: HttpRequest) -> HttpResponse:
    return render(request, "purchase.html")

def purchase(request: HttpRequest) -> HttpResponse:
    return render(request, "purchase.html")
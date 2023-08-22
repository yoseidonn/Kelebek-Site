from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from pages.models import Heading, Feature

# Create your views here.
def introduction(request: HttpRequest) -> HttpResponse:
    return render(request, "program/introduction.html")

def downloads(request: HttpRequest) -> HttpResponse:
    return render(request, "program/downloads.html")

def downloads_details(request: HttpRequest, platform_name: str) -> HttpResponse:
    if platform_name == "windows":
        return render(request, "program/windows.html")
    
    elif platform_name == "linux":
        return render(request, "program/linux.html")

    elif platform_name == "mac":
        return render(request, "program/mac.html")

    else:
        return None
    
def download(request: HttpRequest) -> HttpResponse:
    return render(request, "program/download.html")

def fees(request: HttpRequest) -> HttpResponse:
    return render(request, "program/fees.html")

def purchase_std(request: HttpRequest) -> HttpResponse:
    return render(request, "program/purchase-std.html")

def purchase_pro(request: HttpRequest) -> HttpResponse:
    return render(request, "program/purchase-pro.html")
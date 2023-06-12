from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.
def announcements(request: HttpRequest) -> HttpResponse:
    return render(request, "announcements.html")
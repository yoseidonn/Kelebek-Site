from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Announcement
from pages.models import Heading, Feature


# Create your views here.
def announcement(request: HttpRequest, announcement_id: int) -> HttpResponse:
    try:
        announce = Announcement.objects.get(id=announcement_id)
    except Exception as e:
        announce = None
        
    context = {"announce": announce}
    
    return render(request, "announcements/announcement.html", context)

def announcements(request: HttpRequest) -> HttpResponse:
    announces = Announcement.objects.all().order_by("-date")
    context = {"announces": announces}
    
    return render(request, "announcements/announcements.html", context)

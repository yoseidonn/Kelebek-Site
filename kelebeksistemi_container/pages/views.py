from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Feature, Heading, Slide


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    headings = Heading.objects.all().order_by("date")
    features = Feature.objects.all().order_by("date")
    slides = Slide.objects.all().order_by("-date")
    slides1 = enumerate(slides)
    slides2 = enumerate(slides)
    context = {"headings": headings,"features": features, "slides1": slides1, "slides2": slides2}
    
    return render(request, "pages/index.html", context)
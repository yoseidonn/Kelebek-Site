from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def test(request) -> HttpResponse:
    return render(request, 'test.html')
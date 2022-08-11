from django.shortcuts import render
from django.http import HttpResponse

# This is just the view for the static homepage.
def home(request):
    return render(request, "home.html", {})

def exhibit(request):
    return render(request, "exhibit.html", {})

def aboutus(request):
    return render(request, "aboutus.html", {})
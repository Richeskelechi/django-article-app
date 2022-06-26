from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'aboutpage.html')
    # return HttpResponse("About page")


def home(request):
    return render(request, 'homepage.html')
    # return HttpResponse("Home page")

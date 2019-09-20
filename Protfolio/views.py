from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"home_page.html")

def gallery(request):
    return render(request,"gallery.html")

def protfolio(request):
    return render(request,"protfolio.html")

def contact(request):
    return render(request,"contact.html")
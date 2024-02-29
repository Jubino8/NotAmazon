from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {} #dictionary. This is optional information that we can pass from
    context["Title"] = "This is a test"
    return render(request, "base.html", context)


def products(request):
    return render(request, "products.html",{})

def products(request):
    return render(request, "products.html",{})
def shop(request):
    return render(request, "shop.html",{})

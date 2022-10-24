from django.shortcuts import render
from django.http import HttpResponse


def catalog(request):
    return render(request, 'products/catalog.html')

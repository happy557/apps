from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h1> this is homepage <h1>')
def aboutus(request):
    return HttpResponse('<h1> this is aboutpage <h1>')
def contact(request):
    return HttpResponse('<h1> this is contactpage <h1>')

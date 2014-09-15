from django.shortcuts import render_to_response
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World")
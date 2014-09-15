from django.shortcuts import render_to_response
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response('about.html')

def blog(request):
    return render_to_response('blog.html')

def contact(request):
    return render_to_response('contact.html')
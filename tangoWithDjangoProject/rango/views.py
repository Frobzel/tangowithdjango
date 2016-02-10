from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "this is a bold message"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'anothermessage': "I mean look at these images"}
    return render(request, 'rango/about.html', context_dict)



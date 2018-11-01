from django.shortcuts import render
from django.http import HttpResponse
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def hello(request):
    context = {}
    context['hello'] = 'Hello World!123'
    print(BASE_DIR)
    print(os.path.join(BASE_DIR, 'template'))
    #return HttpResponse("Hello world ! ")
    return render(request, 'hello.html', context)
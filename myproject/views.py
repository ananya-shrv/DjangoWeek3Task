from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, this is my view!")

from django.shortcuts import render

def task_page(request):
    dynamic_message = "Welcome to my dynamic page!"
    return render(request, 'task.html', {'dynamic_message': dynamic_message})


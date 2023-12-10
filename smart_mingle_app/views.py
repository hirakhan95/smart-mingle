from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'home.html')


@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'contact.html')


@require_http_methods(["GET", "POST"])
def create_event(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'create_event.html')

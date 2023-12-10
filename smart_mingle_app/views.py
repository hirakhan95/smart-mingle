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


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'login.html')


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'signup.html')


@require_http_methods(["GET"])
def event(request):
    return render(request, 'event.html')


@require_http_methods(["GET"])
def user(request):
    return render(request, 'user.html')

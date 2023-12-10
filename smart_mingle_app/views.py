from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def home(request):
    return render(request, 'home.html')


@require_http_methods(["GET", "POST"])
def contact(request):
    return render(request, 'contact.html')

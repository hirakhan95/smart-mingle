from django.shortcuts import render


# Create your views here.
def get_main_page(request):
    return render(request, 'smart_mingle/index.html')
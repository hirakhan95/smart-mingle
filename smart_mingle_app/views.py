from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from cloudinary.uploader import upload


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


@login_required
@require_http_methods(["GET", "POST"])
def user(request):
    user = request.user
    if request.method == 'POST':
        image = request.FILES['file']

        # upload_result = upload(image)
        # image_url = upload_result.get('url')

        image_url = 'http://res.cloudinary.com/dpl3nuqof/image/upload/v1702375108/cld-sample-5.jpg'

        user.email = request.POST.get('email', user.email)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        # user.phonenum = request.POST.get('phonenum', user.phonenum)  # Assuming 'phonenum' is a valid user attribute

        user.save()

    context = {
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phonenum': '031-123456',
        'profilepic': 'static/images/user.png'
    }
    return render(request, 'user.html', context=context)



@login_required
@require_http_methods(["GET"])
def user_edit(request):
    user = request.user
    context = {
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phonenum': '031-123456'
    }
    return render(request, 'user_edit.html', context=context)

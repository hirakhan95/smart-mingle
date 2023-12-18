from cloudinary.uploader import upload
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import ExtraDetails, Contact


@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'home.html')


@require_http_methods(["GET"])
def contact(request):
    return render(request, 'contact.html')


@require_http_methods(["POST"])
def contact_success(request):
    if request.method == 'POST':
        contact_message = Contact(name=request.POST['name'], email=request.POST['email'], phone_number=request.POST['phonenum'],
                                  description=request.POST['description'])

        contact_message.save()
    return render(request, 'contact_success.html')


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
    if request.method == 'POST':
        if 'file' in request.FILES:
            image = request.FILES['file']
            upload_result = upload(image,
                                   transformation=[
                                       {'width': 300, 'height': 300, 'gravity': "face", 'crop': "thumb"},
                                       {'radius': "max"},
                                       {'effect': "sharpen"}
                                   ])
            image_url = upload_result.get('url')
        else:
            image_url = None

        extra_details = ExtraDetails.objects.filter(user=request.user).first()
        if not extra_details:
            extra_details = ExtraDetails(user=request.user)

            if image_url is None:
                image_url = "static/images/user.png"
        else:
            if image_url is None:
                image_url = extra_details.display_pic

        extra_details.phone_num = request.POST['phonenum']
        extra_details.display_pic = image_url
        extra_details.save()

        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.save()

        print(extra_details)

    image_url = "static/images/user.png"
    phone_num = ''

    extra_details = ExtraDetails.objects.filter(user=request.user).first()
    if extra_details:
        image_url = extra_details.display_pic
        phone_num = extra_details.phone_num

    context = {
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'phonenum': phone_num,
        'profilepic': image_url
    }
    return render(request, 'user.html', context=context)


@login_required
@require_http_methods(["GET"])
def user_edit(request):
    user = request.user

    extra_details = ExtraDetails.objects.filter(user=user).first()

    image_url = "static/images/user.png"
    phone_num = ''

    if extra_details != None:
        image_url = extra_details.display_pic
        phone_num = extra_details.phone_num

    context = {
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_num': phone_num,
        'profilepic': image_url
    }

    print('abc')
    return render(request, 'user_edit.html', context=context)

from cloudinary.uploader import upload
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import ExtraDetails, Contact, Event


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
        contact_message = Contact(name=request.POST['name'], email=request.POST['email'],
                                  phone_number=request.POST['phonenum'],
                                  description=request.POST['description'])

        contact_message.save()
    return render(request, 'contact_success.html')


@login_required
@require_http_methods(["GET"])
def create_event(request):
    return render(request, 'create_event.html')


@login_required
@require_http_methods(["POST"])
def event_success(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES['image']
            upload_result = upload(image)
            image_url = upload_result.get('url')
        else:
            image_url = None

        event = Event(
            organizer=request.user,
            title=request.POST['title'],
            img_url=image_url,
            description=request.POST['event_description'],
            location=request.POST['location'],
            category=request.POST['category'],
            start_time=request.POST['date'],
            updated_at=request.POST['time'],
        )

        event.save()

        print(request.POST)
    return render(request, 'event_success.html')


@require_http_methods(["GET"])
def event(request, slug):
    event = Event.objects.filter(slug=slug).first()
    suggested_events = Event.objects.order_by('?')[:9]
    context = {
        'event': event,
        'suggested_events_focus': suggested_events[:3],
        'suggested_events_unfocus': suggested_events[3:6],
        'suggested_events_unfocus2': suggested_events[6::]
    }
    return render(request, 'event.html', context=context)


def search(request):
    return render(request, 'search.html')


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


def delete_event(request):
    return render(request, 'delete_event.html', context= {
        'event_id': request.POST['event_id']
    })


def update_event(request):
    return render(request, 'update_event.html')


@login_required
@require_http_methods(["GET", "POST"])
def user(request):
    if request.method == 'POST' and 'event_type' in request.POST and request.POST['event_type'] == 'delete_event':
        Event.objects.filter(id=request.POST['event_id']).first().delete()
    elif request.method == 'POST':
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

    # FOR ALL EVENTS RELATED TO USER

    events = Event.objects.filter(organizer=request.user).values()


    context = {
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'phonenum': phone_num,
        'profilepic': image_url,
        'events': events
    }
    return render(request, 'user.html', context=context)


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

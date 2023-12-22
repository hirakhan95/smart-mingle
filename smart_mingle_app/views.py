from datetime import datetime

from cloudinary.uploader import upload
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ExtraDetails, Contact, Event

EVENT_TYPES = ['Corporate', 'Exhibition', 'Sport', 'Charity', 'Workshop',
               'Virtual', 'Leisure']


@require_http_methods(["GET"])
def home(request):
    events = Event.objects.order_by('?')[:12]

    return render(request, 'home.html', context={
        'event_focus': events[:3],
        'event_unfocus': events[3:6],
        'event_unfocus2': events[6:9],
        'event_unfocus3': events[9::]
    })


@require_http_methods(["GET"])
def contact(request):
    return render(request, 'contact.html')


@require_http_methods(["POST"])
def contact_success(request):
    if request.method == 'POST':
        contact_message = Contact(name=request.POST['name'],
                                  email=request.POST['email'],
                                  phone_number=request.POST['phonenum'],
                                  description=request.POST['description'])

        contact_message.save()
    return render(request, 'contact_success.html')


@login_required
@require_http_methods(["GET"])
def create_event(request):
    return render(request, 'create_event.html', context={
        'categories': EVENT_TYPES
    })


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

        datetime_str = f"{request.POST['date']} {request.POST['time']}"
        event = Event(
            organizer=request.user,
            title=request.POST['title'],
            img_url=image_url,
            description=request.POST['event_description'],
            location=request.POST['location'],
            category=request.POST['category'],
            start_time=datetime.strptime(datetime_str, "%Y-%m-%d %H:%M"),
            updated_at=datetime.now()
        )

        event.save()
    return render(request, 'event_success.html')


@require_http_methods(["GET"])
def event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    suggested_events = Event.objects.order_by('?')[:9]
    context = {
        'event': event,
        'suggested_events_focus': suggested_events[:3],
        'suggested_events_unfocus': suggested_events[3:6],
        'suggested_events_unfocus2': suggested_events[6::]
    }
    return render(request, 'event.html', context=context)


def search(request):
    search_field = request.GET.get('a') or ''
    events = Event.objects.filter(Q(title__icontains=search_field)
                                  | Q(location__icontains=search_field)
                                  | Q(category__icontains=search_field))

    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    return render(request, 'search.html', context={
        'events': events,
        'a': search_field,
        'page': page_number
    })


@require_http_methods(["GET", "POST"])
def login(request):
    return render(request, 'login.html')


@require_http_methods(["GET", "POST"])
def signup(request):
    return render(request, 'signup.html')


@login_required
@require_http_methods(["POST"])
def delete_event(request):
    return render(request, 'delete_event.html', context={
        'event_id': request.POST['event_id']
    })


@login_required
@require_http_methods(["POST"])
def update_event(request):
    error_message = None

    if request.POST.get('call_type') == 'from_update':
        event = get_object_or_404(Event, id=request.POST.get('event_id'))
        datetime_str = f"{request.POST.get('date')} {request.POST.get('time')}"

        event.title = request.POST.get('title')
        if 'image' in request.FILES:
            image = request.FILES['image']
            upload_result = upload(image)  # Ensure 'upload' is defined
            event.img_url = upload_result.get('url')

        event.description = request.POST.get('event_description')
        event.location = request.POST.get('location')
        event.category = request.POST.get('category')
        event.start_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

        try:
            event.full_clean()  # Validates the model
            event.save()
            return redirect('app:event', slug=event.slug)
        except ValidationError as e:
            error_message = str(e)
        except IntegrityError:
            error_message = 'Title already exists! Try with another name!'

    # This part can be removed if you're redirecting after successful save
    event = get_object_or_404(Event, id=request.POST.get('event_id'))
    date_str = event.start_time.strftime('%Y-%m-%d')
    time_str = event.start_time.strftime('%H:%M')

    context = {
        'event': event,
        'categories': EVENT_TYPES,
        'date_str': date_str,
        'time_str': time_str,
        'error_message': error_message,
        'event_id': event.id  # Changed from request.POST to event.id
    }

    return render(request, 'update_event.html', context=context)


@login_required
@require_http_methods(["GET", "POST"])
def user(request):
    if request.method == 'POST' and 'event_type' in request.POST \
            and request.POST['event_type'] == 'delete_event':
        get_object_or_404(Event, id=request.POST['event_id']).delete()
    elif request.method == 'POST':
        if 'file' in request.FILES:
            image = request.FILES['file']
            upload_result = upload(image,
                                   transformation=[
                                       {
                                           'width': 300,
                                           'height': 300,
                                           'gravity': "face",
                                           'crop': "thumb"
                                       },
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

    extra_details = ExtraDetails.objects.filter(user=request.user).first()

    image_url = "static/images/user.png"
    phone_num = ''

    if extra_details is not None:
        image_url = extra_details.display_pic
        phone_num = extra_details.phone_num

    context = {
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_num': phone_num,
        'profilepic': image_url
    }

    return render(request, 'user_edit.html', context=context)


@require_http_methods(["GET", "POST"])
def handler_404(request, *args, **kwargs):
    return render(request, 'error404.html')


@require_http_methods(["GET", "POST"])
def handler_500(request, *args, **kwargs):
    return render(request, 'error500.html')

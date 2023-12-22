import os
from datetime import datetime, timedelta

import pytest
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from smart_mingle_app.models import Event, ExtraDetails


@pytest.fixture(scope='session', autouse=True)
def configure_test_database():
    settings.DATABASES['default']['NAME'] = os.environ['TEST_DB_NAME']
    settings.DATABASES['default']['USER'] = os.environ['TEST_DB_USERNAME']
    settings.DATABASES['default']['PASSWORD'] = os.environ['TEST_DB_PASSWORD']
    settings.DATABASES['default']['HOST'] = os.environ['TEST_DB_HOST']
    settings.DATABASES['default']['PORT'] = os.environ['TEST_DB_PORT']


@pytest.fixture
def create_user(db):
    return User.objects.create_user(username='test_user', password='12345')


@pytest.fixture
def sample_image():
    # Open an actual image file in binary mode
    with open('static/images/event1.jpeg', 'rb') as image:
        return SimpleUploadedFile("test_image.jpeg", image.read(), content_type="image/jpeg")


@pytest.fixture
def create_events(db, create_user):
    events = []
    for i in range(12):
        event = Event.objects.create(
            organizer=create_user,
            title=f'Event {i}',
            img_url=f'http://example.com/event_{i}.jpg',
            description=f'Description for event {i}',
            location=f'Location {i}',
            category=f'Category {i % 4}',
            start_time=datetime.now() + timedelta(days=i),
        )
        events.append(event)
    return events


@pytest.fixture
def create_event(db, create_user):
    return Event.objects.create(
        organizer=create_user,
        title='Test Event',
        img_url='http://example.com/test.jpg',
        description='This is a test event',
        location='Test Location',
        category='Test Category',
        start_time=datetime.now()
    )


@pytest.fixture
def create_events_search(db, create_user):
    titles = ['Event1', 'Event2', 'Event3', 'Event4', 'Event5', 'Event6']
    for title in titles:
        Event.objects.create(
            organizer=create_user,
            title=title,
            img_url='http://example.com/event.jpg',
            description='Description for ' + title,
            location='Location ' + title[-1],
            category='Category ' + title[-1],
            start_time=datetime.now()
        )


@pytest.fixture
def user_with_extras(db):
    user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')
    ExtraDetails.objects.create(
        user=user,
        phone_num='1234567890',
        display_pic='http://example.com/user.jpg'
    )
    return user

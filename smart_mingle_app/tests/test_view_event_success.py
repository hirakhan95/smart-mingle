import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_event_success_unauthenticated(client):
    url = reverse('app:event_success')
    response = client.post(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('account_login'))


@pytest.mark.django_db
def test_event_success_authenticated(client, create_user, sample_image):
    client.force_login(create_user)
    url = reverse('app:event_success')
    post_data = {
        'title': 'Test Event',
        'event_description': 'This is a test event',
        'location': 'Test Location',
        'category': 'Test Category',
        'date': '2023-01-01',
        'time': '12:00',
        'image': sample_image,
    }
    response = client.post(url, post_data)
    assert response.status_code == 200
    assert 'event_success.html' in [t.name for t in response.templates]

    # Verify that an Event instance was created
    from smart_mingle_app.models import Event  # Import your Event model
    assert Event.objects.filter(title='Test Event').exists()

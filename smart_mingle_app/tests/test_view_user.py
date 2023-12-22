import pytest
from django.urls import reverse

from smart_mingle_app.models import Event


@pytest.mark.django_db
def test_user_view_get_request(client, create_user):
    client.force_login(create_user)
    url = reverse('app:user')
    response = client.get(url)
    assert response.status_code == 200
    assert 'user.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_user_view_post_update_profile(client, create_user, sample_image):
    client.force_login(create_user)
    url = reverse('app:user')
    post_data = {
        'first_name': 'NewFirstName',
        'last_name': 'NewLastName',
        'phonenum': '1234567890',
        'file': sample_image
    }
    response = client.post(url, post_data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_view_post_delete_event(client, create_user, create_event):
    client.force_login(create_user)
    event = create_event
    url = reverse('app:user')
    post_data = {
        'event_type': 'delete_event',
        'event_id': event.id
    }
    response = client.post(url, post_data)
    assert response.status_code == 200
    assert not Event.objects.filter(id=event.id).exists()

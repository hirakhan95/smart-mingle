import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_update_event_view(client, create_user, create_event):
    client.force_login(create_user)
    url = reverse('app:update_event')
    event = create_event

    valid_update_data = {
        'call_type': 'from_update',
        'event_id': event.id,
        'title': 'Updated Event',
        'event_description': 'Updated Description',
        'location': 'Updated Location',
        'category': 'Category1',
        'date': '2023-01-01',
        'time': '12:00'
    }
    response = client.post(url, valid_update_data)

    assert response.status_code == 302

    invalid_update_data = {
        'call_type': 'from_update',
        'event_id': event.id,
        'title': 'Updated Event',
        'event_description': 'Updated Description',
        'location': 'Updated Location',
        'category': 'Category',
        'date': '2023-01-01',
        'time': '12:00'
    }
    response = client.post(url, invalid_update_data)
    assert response.status_code == 302

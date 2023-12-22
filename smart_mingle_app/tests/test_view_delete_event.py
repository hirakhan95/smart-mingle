import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_delete_event_view(client, create_user):
    client.force_login(create_user)
    url = reverse('app:delete_event')

    # Assuming you have an event to delete with ID 1
    post_data = {'event_id': 1}
    response = client.post(url, post_data)

    assert response.status_code == 200
    assert 'delete_event.html' in [t.name for t in response.templates]
    assert response.context['event_id'] == '1'

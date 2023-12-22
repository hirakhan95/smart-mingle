import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_view(client, create_events):
    create_events

    url = reverse('app:home')
    response = client.get(url)

    assert response.status_code == 200
    assert 'home.html' in [t.name for t in response.templates]

    assert len(response.context['event_focus']) == 3
    assert len(response.context['event_unfocus']) == 3
    assert len(response.context['event_unfocus2']) == 3
    assert len(response.context['event_unfocus3']) == 3

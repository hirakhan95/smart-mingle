import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_event_unauthenticated(client):
    url = reverse('app:create_event')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('account_login'))


@pytest.mark.django_db
def test_create_event_authenticated(client, create_user):
    client.force_login(create_user)
    url = reverse('app:create_event')
    response = client.get(url)
    assert response.status_code == 200
    assert 'create_event.html' in [t.name for t in response.templates]
    assert 'categories' in response.context

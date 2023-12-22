import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_search_view(client, create_events_search):
    create_events_search

    response = client.get(reverse('app:search'), {'a': 'Event1'})
    assert response.status_code == 200
    assert 'search.html' in [t.name for t in response.templates]
    assert len(response.context['events']) == 1
    assert response.context['events'][0].title == 'Event1'

    response = client.get(reverse('app:search'), {'a': '', 'page': 2})
    assert response.context['page'] == '2'
    assert len(response.context['events']) <= 5
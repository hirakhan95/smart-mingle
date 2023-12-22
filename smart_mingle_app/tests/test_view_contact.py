import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_contact_view(client):
    url = reverse('app:contact')
    response = client.get(url)
    assert response.status_code == 200

    assert 'contact.html' in [t.name for t in response.templates]
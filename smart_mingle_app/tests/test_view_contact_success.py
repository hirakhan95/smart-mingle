import pytest
from django.urls import reverse

from smart_mingle_app.models import Contact


@pytest.mark.django_db
def test_contact_success_view(client):
    url = reverse('app:contact_success')
    contact_data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'phonenum': '1234567890',
        'description': 'Test message'
    }
    response = client.post(url, contact_data)
    assert response.status_code == 200

    assert Contact.objects.filter(email='john@example.com').exists()

    assert 'contact_success.html' in [t.name for t in response.templates]

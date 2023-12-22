import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_event_view(client, create_event):
    event = create_event
    url = reverse('app:event', kwargs={'slug': event.slug})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['event'] == event
    assert 'event.html' in [t.name for t in response.templates]

    # Verify context for suggested events
    assert 'suggested_events_focus' in response.context
    assert 'suggested_events_unfocus' in response.context
    assert 'suggested_events_unfocus2' in response.context

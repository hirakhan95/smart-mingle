import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_user_edit_view_with_extras(client, user_with_extras):
    client.force_login(user_with_extras)
    url = reverse('app:user_edit')
    response = client.get(url)

    assert response.status_code == 200
    assert 'user_edit.html' in [t.name for t in response.templates]
    assert response.context['email'] == user_with_extras.email
    assert response.context['phone_num'] == '1234567890'
    assert response.context['profilepic'] == 'http://example.com/user.jpg'


@pytest.mark.django_db
def test_user_edit_view_without_extras(client, create_user):
    client.force_login(create_user)
    url = reverse('app:user_edit')
    response = client.get(url)

    assert response.status_code == 200
    assert 'user_edit.html' in [t.name for t in response.templates]
    assert response.context['email'] == create_user.email
    assert response.context['phone_num'] == ''
    assert response.context['profilepic'] == "static/images/user.png"

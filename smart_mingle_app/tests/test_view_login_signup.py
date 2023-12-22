import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_login_view_get_request(client):
    url = reverse('account_login')
    response = client.get(url)
    assert response.status_code == 200
    assert 'account/login.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_login_view_post_request(client):
    url = reverse('account_login')
    post_data = {'username': 'testuser', 'password': 'password123'}
    response = client.post(url, post_data)
    assert response.status_code == 200
    assert 'account/login.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_signup_view_get_request(client):
    url = reverse('account_signup')
    response = client.get(url)
    assert response.status_code == 200
    assert 'account/signup.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_signup_view_post_request(client):
    url = reverse('account_signup')
    post_data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword123'}
    response = client.post(url, post_data)
    assert response.status_code == 200
    assert 'account/signup.html' in [t.name for t in response.templates]

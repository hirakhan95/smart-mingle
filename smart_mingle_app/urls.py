from django.urls import path
from smart_mingle_app import views as app

app_name = 'smart_mingle_app'


urlpatterns = [
    path('', app.home, name='home'),
    path('contact', app.contact, name='contact'),
    path('create_event', app.create_event, name='create_event'),
    path('login', app.login, name='login'),
    path('signup', app.signup, name='signup'),
    path('event', app.event, name='event'),
    path('user', app.user, name='user'),
]

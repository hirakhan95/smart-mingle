from django.urls import path
from smart_mingle_app import views

app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us', views.contact, name='contact'),
    path('create_event', views.create_event, name='create_event'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('event', views.event, name='event'),
    path('user', views.user, name='user'),
    path('user_edit', views.user_edit, name='user_edit'),
]

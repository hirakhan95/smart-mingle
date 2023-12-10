from django.urls import path
from smart_mingle_app import views as app

app_name = 'smart_mingle_app'


urlpatterns = [
    path('', app.home, name='home'),
    path('contact', app.contact, name='contact'),
]

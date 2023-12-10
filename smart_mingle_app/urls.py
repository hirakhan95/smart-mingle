from django.urls import path
from smart_mingle_app.views import home

app_name = 'smart_mingle_app'


urlpatterns = [
    path('', home, name='home')
]

"""smart_mingle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('smart_mingle_app.urls'))
]

handler404 = 'smart_mingle_app.views.handler_404'
handler500 = 'smart_mingle_app.views.handler_500'
handler405 = 'smart_mingle_app.views.handler_500'
handler403 = 'smart_mingle_app.views.handler_500'
handler400 = 'smart_mingle_app.views.handler_500'
handler401 = 'smart_mingle_app.views.handler_500'
handler502 = 'smart_mingle_app.views.handler_500'

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

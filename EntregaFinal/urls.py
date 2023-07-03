from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from BlogFinal import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('BlogFinal/', include('BlogFinal.urls')),
    path('', RedirectView.as_view(url='/BlogFinal/', permanent=True)),
    path('inicio', RedirectView.as_view(url='/BlogFinal/inicio', permanent=True)),
    path('login', RedirectView.as_view(url='/BlogFinal/login', permanent=True)),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

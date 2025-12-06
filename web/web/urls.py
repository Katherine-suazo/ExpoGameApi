from django.contrib import admin
from django.urls import path, include
from  django.conf import settings


urlpatterns = [

    path('',include('core.urls')),

    path('novedades/',include('novedades.urls')),

    path('solicitud/', include('solicitud.urls')),

    path('contacto/', include('login.urls')),
    
    path('admin/', admin.site.urls),

]

if settings.DEBUG: #
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # para que las imagenes se vean en el navegador en modo debug



from django.conf import settings
from . import views
from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about_us, name='about_us'),
    path('contact/',views.contact_us, name='contact_us'),
    path('products/',include('store.urls')),
    path('',include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

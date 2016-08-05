from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/',include('myproject.myapp.urls')),
    url(r'^fuck/',include('myproject.fuck.urls')),

    url(r'^$', RedirectView.as_view(url='/myapp/list/', permanent=True)),
    # url(r'^myapp/fuck/$',RedirectView.as_view(url='/myapp/list/', permanent=True)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

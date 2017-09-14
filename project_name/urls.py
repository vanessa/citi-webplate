from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('core.urls', namespace='core')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^admin/', admin.site.urls),
]

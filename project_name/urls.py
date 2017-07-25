from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('core.urls', namespace='core')),
    url(r'^', include('accounts.urls', namespace='accounts')),
    #url(r'^admin/', admin.site.urls),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BaseView.as_view(), name='index'),
]

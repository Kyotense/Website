from django.conf.urls import url

from . import views

app_name = 'shop'
urlpatterns = [
    url(r'^(?P<username>\w{0,50})$', views.IndexView.as_view(), name='index'),
]
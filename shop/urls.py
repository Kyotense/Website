from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

app_name = 'shop'
urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='staticpages/index.html'), name='home'),
    url(r'^shop/(?P<username>\w{0,50})$', views.ShopView.as_view(), name='shop'),
]
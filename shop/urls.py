from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

app_name = 'shop'
urlpatterns = [
	url(r'^$', views.ShopIndexView.as_view()),#TemplateView.as_view(template_name='staticpages/index.html'), name='home'),
    url(r'^shop/(?P<category>[a-zA-Z]*(| [a-zA-Z]*))$', views.ShopView.as_view(), name='shop'),
    url(r'^shop/(?P<pk>[1-9][0-9]*)',views.ProductView.as_view(), name = 'productview'),
    url(r'^about', TemplateView.as_view(template_name='staticpages/about.html'), name='about')
]
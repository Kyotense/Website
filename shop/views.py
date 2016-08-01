from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Product

# a generic class provided by the first django tutorial
class ShopView(generic.ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    model = Product
    order = ["company","description","pub_date","name","price","company__company_name"]

    def pages(self):
    	"""Returns the maximum possible number of pages."""
    	return int(len(Product.objects.all())/6) + 1
    def get_queryset(self):
        """Change me"""

        order_by = "pub_date"

        start = 0
        end = 6

        # www.google.com/something/blah/?order_by=whatever
        if self.request.GET.get("order_by"):
        	order_by = (self.request.GET.get("order_by"))

        	if not order_by in self.order:
        		order_by = "pub_date"
       	if self.request.GET.get("page"):
       		page = int(self.request.GET.get("page"))
       		start = (page-1)*6
       		end = 6 * page
      	# urls view can be used for args and kwargs...
        #print (self.username)
        return Product.objects.order_by(order_by)[start:end] #filter(pub_date__lte=timezone.now())
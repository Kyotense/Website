from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Product

# a generic class provided by the first django tutorial
class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'products'
    model = Product
    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
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
    limit = 2
    numitems = 3
    def pages(self):
      """Returns the maximum possible number of pages."""
      return int(len(Product.objects.all())/self.numitems) + 1
    def previous(self):
      page = 0
      if self.request.GET.get("page"):
        page = int(self.request.GET.get("page"))
      if page != None and page > 1:
          page -= 1
      return page
    def current(self):
      page = 0
      if self.request.GET.get("page"):
        page = int(self.request.GET.get("page"))
      return page
    def next(self):
      page = 0
      if self.request.GET.get("page"):
        page = int(self.request.GET.get("page"))
      if page != None and page < self.pages():
          page += 1
      return page
    def first(self):
      return 1
    def last(self):
      return self.pages()
    def pagination(self):
      numpages = self.pages()
      page = 1

      if self.request.GET.get("page"):
          page = int(self.request.GET.get("page"))

      page = page - 1

      page = page - page % self.limit

      if page  <= 0:
        page = 1
      end = page + self.limit-1 if page + self.limit-1 <= numpages else numpages

      outlist = range(page,end+1)

      return range(page,end+1)
    def get_queryset(self):
        """Change me"""

        order_by = "pub_date"

        start = 0
        end = self.numitems

        # www.google.com/something/blah/?order_by=whatever
        if self.request.GET.get("order_by"):
        	order_by = (self.request.GET.get("order_by"))

        	if not order_by in self.order:
        		order_by = "pub_date"
       	if self.request.GET.get("page"):
       		page = int(self.request.GET.get("page"))
       		start = (page-1)*self.numitems
       		end = self.numitems * page
      	# urls view can be used for args and kwargs...
        #print (self.username)
        return Product.objects.order_by(order_by)[start:end] #filter(pub_date__lte=timezone.now())
class ProductView(generic.DetailView):
  context_object_name = "product"
  template_name = 'shop/productdetail.html'
  def get_queryset(self):
    print self.args
    return Product.objects

'''def get_product(request,product_id):
  product = get_object_or_404(Product, pk=product_id)
  try:
    selected_product = product.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
  else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('shop:product_listing', args=(product.id,)))'''
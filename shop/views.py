from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Product, Category

class ShopView(generic.ListView):
    '''
      Class name: ShopView
      Descritpion: This class is responsible for handing all shop interactions.
    '''
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    model = Product
    order = ["company","description","pub_date","name","price","company__company_name"]
    limit = 4 # number of items on the page bar
    numitems = 6 # number of items to throw on the page
    def pages(self):
      """Returns the maximum possible number of pages."""
      items = Product.objects.all()
      if "category" in self.kwargs:
        items = Product.objects.filter(category__name__contains=self.kwargs["category"])#[start:end]
      else:
        items = Product.objects#[start:end]
      return int(len(items.all())/self.numitems) + 1
    def previous(self):
      page = 1
      if self.request.GET.get("page"):
        page = int(self.request.GET.get("page"))
      if page != None and page > 1:
          page -= 1
      return page
    def current(self):
      page = 1
      if self.request.GET.get("page"):
        print ("PAGE")
        print (page)
        page = int(self.request.GET.get("page"))
      return page
    def next(self):
      page = 1
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
        print (self.kwargs)
        if "category" in self.kwargs:
          return Product.objects.order_by(order_by).filter(category__name__contains=self.kwargs["category"])[start:end]
        else:
          return Product.objects.order_by(order_by)[start:end] #filter(pub_date__lte=timezone.now())

    # Not necessary
    def get_context_data(self, **kwargs):
        context = super(ShopView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductView(generic.DetailView):
  context_object_name = "product"
  template_name = 'shop/productdetail.html'
  def get_queryset(self):
    #print self.args
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
class ShopIndexView(ShopView):
  context_object_name = "product"
  template_name = 'shop/index.html'

  def firstitem(self):
    order_by = "pub_date"
    return Product.objects.order_by(order_by)[0]
  def carousel(self):
    order_by = "pub_date"
    return Product.objects.order_by(order_by)[1:5]
    
  def get_queryset(self):
    return Product.objects

  def nextten(self):
    #print (len(Product.objects.order_by("pub_date")[5:16]))
    return Product.objects.order_by("pub_date")[5:16]
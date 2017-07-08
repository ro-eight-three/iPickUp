from django.core.exceptions import SuspiciousOperation
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, CreateView, FormView
from sellers.models import Seller
from common.views import FilteredListView
from .models import Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'descirption')

    def form_valid(self, form):
        qo_sellers = Seller.objects.filter(user=self.request.user)
        if len(qo_sellers) == 1:
            form.instance.seller = qo_sellers[0]
            return super(CreateView, self).form_valid(form)
        raise SuspiciousOperation('creating product without user')

    def get_success_url(self):
        return reverse('products:list')


class ProductListView(FilteredListView):
    model = Product
    queryset = Product.objects.all()
    paginate_by = 10

    def get_filter_queryset(self, queryset, q):
        return queryset.filter(name__icontains=q)


class ProductListFromSellerView(ProductListView):
    def get_queryset(self):
        queryset = super().get_queryset()

        seller_id_string = self.kwargs['pk']
        if seller_id_string:
            seller_id = int(seller_id_string)
            self.seller_object = get_object_or_404(Seller, id=seller_id)
            queryset = queryset.filter(seller=self.seller_object)
        else:
            self.seller_object = None

        return queryset

    def get_context_data(self, **kwargs):
        if self.seller_object:
            kwargs['seller'] = self.seller_object
        return super().get_context_data(**kwargs)

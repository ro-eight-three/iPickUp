from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from sellers.models import Seller
from products.models import Product


class DashboardView(View):
    def get(self, request, *args, **kwargs):
        sellers = Seller.objects.order_by('presentation_name')[:5]
        products = Product.objects.order_by('name')[:5]
        return render(request, "common/dashboard.html",
                      {"sellers": sellers,
                       "products": products})


def success_view(request):
    return HttpResponse("success")


class FilteredListView(ListView):
    def get_filter_queryset(self, queryset, q):
        raise NotImplementedError

    def get_queryset(self):
        self.q = self.request.GET.get('q')
        if self.q:
            return self.get_filter_queryset(super().get_queryset(), self.q)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        if self.q:
            kwargs['q'] = self.q
        return super().get_context_data(**kwargs)

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, FormView
from common.views import FilteredListView
from .models import Seller


class SellerDetailView(DetailView):
    model = Seller


class SellerListView(FilteredListView):
    model = Seller
    queryset = Seller.objects.order_by('presentation_name')
    paginate_by = 10

    def get_filter_queryset(self, queryset, q):
        return queryset.filter(presentation_name__icontains=q)

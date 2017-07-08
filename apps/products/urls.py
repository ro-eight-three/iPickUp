from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"^$",  #
        view=views.ProductListView.as_view(),
        name="list"),
    url(
        regex=r"^from/(?P<pk>\d+)/$",  #
        view=views.ProductListFromSellerView.as_view(),
        name="list-seller"),
    url(
        regex=r"^(?P<pk>\d+)/$",  #
        view=views.ProductDetailView.as_view(),
        name="detail"),
    url(
        regex=r"^create/$",  #
        view=views.ProductCreateView.as_view(),
        name="create"),
]

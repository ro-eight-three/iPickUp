from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"^$",  #
        view=views.SellerListView.as_view(),
        name="list"),
    url(
        regex=r"^(?P<pk>\d+)/$",  #
        view=views.SellerDetailView.as_view(),
        name="detail"),
]

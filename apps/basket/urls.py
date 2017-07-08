from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"^$",  #
        view=views.BasketListView.as_view(),
        name="list"),
]

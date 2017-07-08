from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"^$",  #
        view=views.DashboardView.as_view(),
        name="dashboard"),
    url(
        regex=r"^success$",  #
        view=views.success_view,
        name="success"),
]

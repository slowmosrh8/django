from django.conf.urls import url
from . import views
urlpattern=[
    url('',views.HomePageView.as_view(),name='home')]
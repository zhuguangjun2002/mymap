# -*- coding: UTF-8 -*-

from django.conf.urls import include,url 

#from views import HomePageView,county_datasets,point_datasets,point_datasets_02,get_location
from views import HomePageView,MapPageView,county_datasets,point_datasets,point_datasets_02,get_location

from . import views


urlpatterns = [
  #url(r'^$',MapPageView.as_view(),name= 'map'),
  #url(r'^$',HomePageView.as_view(),name= 'home'),
  url(r'^$', views.fiberbox_list, name='fiberbox_list'),
  url(r'^map/$',MapPageView.as_view(),name= 'map'),
  url(r'^county_data/$',county_datasets,name= 'county'),
  # zhuguangjun
  url(r'^fiberboxes/$', point_datasets, name = 'fiberboxes'),
  #url(r'^incidence_data/$',HomePageView.as_view(),name= 'incidence'),
  url(r'^fiberbox_data_02/$', point_datasets_02, name = 'fiberbox_02'),
  # 调用方式：
  # http://localhost:8000/location/{经度},{维度}/
  # 例如：
  # http://localhost:8000/location/121.3929,37.5258/
  url(r'^location/(?P<lonlat>\-?\d+\.\d+\,\-?\d+\.\d+)/$',get_location,name='location'),
]

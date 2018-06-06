# -*- coding: UTF-8 -*-

from django.conf.urls import include,url

from . import views

urlpatterns = [

  # 我们不`对外`提供`混合型`的`fiberbox_list`
  #url(r'^$', views.fiberbox_list, name='fiberbox_list'),
  #url(r'^fiberbox/$', views.fiberbox_list, name='fiberbox_list'),
  # 对外，只提供`firberbox_publish_list`;
  # `登录通过`的`用户`，可以通过点击`草稿图标`，可以查看`草稿列表`
  url(r'^$', views.fiberbox_publish_list, name='fiberbox_publish_list'),
  #url(r'^fiberbox/publish/$', views.fiberbox_publish_list,name='fiberbox_publish_list'),
  url(r'^fiberbox/drafts/$', views.fiberbox_draft_list, name='fiberbox_draft_list'),
  url(r'^fiberbox/new/$', views.fiberbox_new, name='fiberbox_new'),
  url(r'^fiberbox/(?P<pk>\d+)/$', views.fiberbox_detail, name='fiberbox_detail'),
  url(r'^fiberbox/(?P<pk>[0-9]+)/edit/$', views.fiberbox_edit, name='fiberbox_edit'),
  url(r'^fiberbox/(?P<pk>\d+)/remove/$', views.fiberbox_remove, name='fiberbox_remove'),
  url(r'^fiberbox/(?P<pk>\d+)/publish/$',
    views.fiberbox_publish, name='fiberbox_publish'),
  url(r'^fiberbox_map/$',views.fiberbox_map,name= 'fiberbox_map'),
  url(r'^fiberbox_publish_map/$',views.fiberbox_publish_map,name='fiberbox_publish_map'),
  url(r'^fiberbox_draft_map/$',views.fiberbox_draft_map,name= 'fiberbox_draft_map'),
  url(r'^county_data/$',views.county_datasets,name= 'county'),
  # GeoJson Data
  url(r'^fiberbox_data/$', views.fiberbox_data, name = 'fiberbox_data'),
  url(r'^fiberbox_publish_data/$', views.fiberbox_publish_data,name='fiberbox_publish_data'),
  url(r'^fiberbox_drafts_data/$', views.fiberbox_draft_data, name = 'fiberbox_draft_data'),
  url(r'^fiberbox_data_02/$', views.fiberbox_data_02, name = 'fiberbox_02'),
  # 调用方式：
  # http://localhost:8000/location/{经度},{维度}/
  # 例如：
  # http://localhost:8000/location/121.3929,37.5258/
  url(r'^location/(?P<lonlat>\-?\d+\.\d+\,\-?\d+\.\d+)/$',views.get_location,name='location'),
]

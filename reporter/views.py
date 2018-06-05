# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from models import Counties
from models import FiberBox


from django.contrib.gis.geos import GEOSGeometry, LineString, Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth.decorators import login_required  
from django.utils import timezone

# Create your views here.

def fiberbox_list(request):
    boxes = FiberBox.objects.filter(
        updated_at__lte=timezone.now()).order_by('updated_at')
    return render(request, 'reporter/fiberbox_list.html', {'boxes': boxes})


#@login_required
class HomePageView(TemplateView):
    template_name =  'index.html'

class MapPageView(TemplateView):
    template_name =  'map.html'

def county_datasets(request):
    counties = serialize('geojson',Counties.objects.all())
    return HttpResponse(counties,content_type='json')

def point_datasets(request):
    # points = serialize('geojson', FiberBox.objects.all())
    # 控制生成的geojson,只包含客户感兴趣的字段。
    # add field to only display name, 
    # not show `updated_at`,`created-at`, `pk`
    points = serialize('geojson',FiberBox.objects.all(),fields=('name','location'))
    return HttpResponse(points,content_type='json')

def point_datasets_02(request):
    # 添加支持搜寻指定`基准点`
    
    # 国贸大厦
    # pnt = GEOSGeometry('POINT (121.3997 37.5370)',4326)

    # 国贸大厦  
    # pnt = GEOSGeometry('POINT (121.3929 37.5258)',4326)

    # GeoJson格式
    # 国贸大厦
    # pnt = GEOSGeometry('{ "type": "Point", "coordinates": location}') # GeoJSON
    # pnt = GEOSGeometry('POINT (121.3929 37.5258)',4326)
    lonlat = [121.3929,37.5258]
    pnt = Point(lonlat)
    # 根本不需要再去用`GEOSGeometry`初始化一下。
    # 这样做也可以
    # pnt = GEOSGeometry(pnt)

    # 这样做，有问题。
    # pnt = GEOSGeometry('{ "type": "Point", "coordinates": location}') # GeoJSON

    # 方圆半径`1公里`范围内的点
    qs = FiberBox.objects.filter(location__distance_lte=(pnt, D(km=1)))

    # 方圆半径`500米`范围内的点
    # qs = FiberBox.objects.filter(location__distance_lte=(pnt, D(km=0.5)))

    # 方圆半径`2公里`范围内的点
    # qs = FiberBox.objects.filter(location__distance_lte=(pnt, D(km=2)))

    # 方圆半径`5公里`范围内的点
    # qs = FiberBox.objects.filter(location__distance_lte=(pnt, D(km=5)))

    points = serialize('geojson', qs)
    return HttpResponse(points,content_type='json')


def str2cords(lonlat):
    return [float(c) for c in lonlat.split(',')] #or maybe just scords.split(',') since float might mess up the exact cords?


def get_location(request,lonlat):
    """
    调用方式：
    http://localhost:8000/location/{经度},{维度}/
    例如：
    http://localhost:8000/location/121.3929,37.5258/

    """
    # my_location = str2cords(lonlat)
    
    print(lonlat)
    location = str2cords(lonlat)
    # return HttpResponse("my location is %s." % lonlat)
    # return HttpResponse("my location is %s." % location)
    pnt = Point(location)    
    # GeoJSON 格式不好用
    # # pnt = GEOSGeometry('POINT (121.3929 37.5258)',4326)
    # # pnt = GEOSGeometry('{ "type": "Point", "coordinates": [ 5.000000, 23.000000 ] }') # GeoJSON
    # location = [121.3929,37.5258]
    # pnt = GEOSGeometry('{ "type": "Point", "coordinates": location}') # GeoJSON
    qs = FiberBox.objects.filter(location__distance_lte=(pnt, D(km=1)))
    points = serialize('geojson', qs)
    return HttpResponse(points,content_type='json')
    
      

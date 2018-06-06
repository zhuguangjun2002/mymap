# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from models import Counties
from models import Fiberbox


from django.contrib.gis.geos import GEOSGeometry, LineString, Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import FiberboxForm

# Create your views here.

def fiberbox_list(request):
    boxes = Fiberbox.objects.filter(
        updated_at__lte=timezone.now()).order_by('updated_at')
    return render(request, 'reporter/fiberbox_list.html', {'boxes': boxes})


def fiberbox_map(request):
    data_url = 'fiberbox_data'
    context = {'data_url': data_url }
    return render(request,'reporter/fiberbox_map.html',context)

def fiberbox_publish_map(request):
    data_url = 'fiberbox_publish_data'
    context = {'data_url': data_url }
    return render(request,'reporter/fiberbox_map.html',context)

def fiberbox_draft_map(request):
    data_url = 'fiberbox_draft_data'
    context = {'data_url': data_url }
    return render(request,'reporter/fiberbox_map.html',context)

#@login_required
class HomePageView(TemplateView):
    template_name =  'index.html'

def county_datasets(request):
    counties = serialize('geojson',Counties.objects.all())
    return HttpResponse(counties,content_type='json')

def fiberbox_data(request):
    # points = serialize('geojson', Fiberbox.objects.all())
    # 控制生成的geojson,只包含客户感兴趣的字段。
    # add field to only display name,
    # not show `updated_at`,`created-at`, `pk`
    points = serialize('geojson',Fiberbox.objects.all(),fields=('name','location'))
    return HttpResponse(points,content_type='json')

def fiberbox_publish_data(request):
    # points = serialize('geojson', Fiberbox.objects.all())
    # 控制生成的geojson,只包含客户感兴趣的字段。
    # add field to only display name,
    # not show `updated_at`,`created-at`, `pk`
    points = serialize('geojson',Fiberbox.objects.filter(published_date__isnull=False),fields=('name','location'))
    return HttpResponse(points,content_type='json')

def fiberbox_draft_data(request):
    # points = serialize('geojson', Fiberbox.objects.all())
    # 控制生成的geojson,只包含客户感兴趣的字段。
    # add field to only display name,
    # not show `updated_at`,`created-at`, `pk`
    points = serialize('geojson',Fiberbox.objects.filter(published_date__isnull=True),fields=('name','location'))
    return HttpResponse(points,content_type='json')

def fiberbox_data_02(request):
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
    qs = Fiberbox.objects.filter(location__distance_lte=(pnt, D(km=1)))

    # 方圆半径`500米`范围内的点
    # qs = Fiberbox.objects.filter(location__distance_lte=(pnt, D(km=0.5)))

    # 方圆半径`2公里`范围内的点
    # qs = Fiberbox.objects.filter(location__distance_lte=(pnt, D(km=2)))

    # 方圆半径`5公里`范围内的点
    # qs = Fiberbox.objects.filter(location__distance_lte=(pnt, D(km=5)))

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
    qs = Fiberbox.objects.filter(location__distance_lte=(pnt, D(km=1)))
    points = serialize('geojson', qs)
    return HttpResponse(points,content_type='json')

@login_required
def fiberbox_draft_list(request):
    boxes = Fiberbox.objects.filter(
        published_date__isnull=True).order_by('updated_at')
    return render(request, 'reporter/fiberbox_draft_list.html', {'boxes': boxes})


@login_required
def fiberbox_publish(request, pk):
    fiberbox = get_object_or_404(Fiberbox, pk=pk)
    fiberbox.publish()
    return redirect('fiberbox_detail', pk=pk)


@login_required
def fiberbox_new(request):
    if request.method == "POST":
        form = FiberboxForm(request.POST)
        if form.is_valid():
            fiberbox = form.save(commit=False)
            fiberbox.author = request.user
            # fiberbox.published_date = timezone.now()
            fiberbox.save()
            return redirect('fiberbox_detail', pk=fiberbox.pk)
    else:
        form = FiberboxForm()
    return render(request, 'reporter/fiberbox_edit.html', {'form': form})


def fiberbox_detail(request, pk):
    box = get_object_or_404(Fiberbox, pk=pk)
    return render(request, 'reporter/fiberbox_detail.html', {'box': box})

@login_required
def fiberbox_edit(request, pk):
    box = get_object_or_404(Fiberbox, pk=pk)
    if request.method == "POST":
        form = FiberboxForm(request.POST, instance=box)
        if form.is_valid():
            box = form.save(commit=False)
            box.author = request.user
            # box.published_date = timezone.now()
            box.save()
            return redirect('fiberbox_detail', pk=box.pk)
    else:
        form = FiberboxForm(instance=box)
    return render(request, 'reporter/fiberbox_edit.html', {'form': form})

@login_required
def fiberbox_remove(reques, pk):
    # delete a fiberbox
    box = get_object_or_404(Fiberbox, pk=pk)
    box.delete()
    return redirect('fiberbox_list')


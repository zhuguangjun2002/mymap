# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone

# Create your models here.


class FiberBox(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    #address = models.CharField(max_length=50,blank=True,verbose_name='地址')
    village = models.CharField(
        max_length=50, blank=True, verbose_name='村（社区居委会）')
    town = models.CharField(
        max_length=50, blank=True, verbose_name='乡镇（街道办事处）')
    location = models.PointField(srid=4326, verbose_name='位置')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE,verbose_name='创建者')
    published_date = models.DateTimeField(blank=True, null=True,
                                          verbose_name='发布日期')

    objects = models.GeoManager()

    def publish(self):
        self.published_date = timezone.now()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '光纤箱'
        verbose_name_plural = "光纤箱"
        #verbose_name_plural = " FiberBox"
        ordering = ("-updated_at", )


class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.counties

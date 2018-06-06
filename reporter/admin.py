# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Fiberbox, Counties

# Register your models here.

class FiberboxAdmin(LeafletGeoAdmin):
    #list_display = ('name','created_at','updated_at','location')
    list_display = ('name','town','village','updated_at','published_date')
    search_fields = ['name','town','village']
    list_filter = ['town']
    #list_filter = ['updated_at']
    #list_filter = ['created_at']
    ordering = ('-updated_at',)
    date_hierarchy = 'updated_at'

class CountiesAdmin(LeafletGeoAdmin):
    #pass
    list_display = ('counties','codes') # see models.py, class Counties


admin.site.register(Fiberbox,FiberboxAdmin)

# 我们暂时不需要加入`乡镇`的`边界`
#admin.site.register(Counties,CountiesAdmin)

import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

from django.contrib.gis import geos
from .models import Fiberbox

countie_mapping = {
    'counties' : 'Counties',
    'codes' : 'Codes',
    'cty_code' : 'Cty_CODE',
    'dis' : 'dis',
    'geom' : 'MULTIPOLYGON',
}


county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/counties.shp'))


def run(verbose=True):
	lm = LayerMapping(Counties,county_shp,countie_mapping,transform=False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)


fiberboxes_csv = os.path.abspath(os.path.join('data', 'fiberboxes.csv'))

def fiberboxes_load():
    with open(fiberboxes_csv) as point_file:
        for line in point_file:
            name, lon, lat = line.split(',')
            point = "POINT(%s %s)" % (lat.strip(), lon.strip())
            Point.objects.create(name=name, geom=geos.fromstr(point))

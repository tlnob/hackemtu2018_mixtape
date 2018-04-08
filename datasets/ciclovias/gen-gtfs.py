#!/usr/bin/env python

from shapefile import Reader as Shp
from simpledbf import Dbf5 as Dbf
from glob import glob

trips = []
shapes = []

for name in glob('*.dbf'):
    dbf = Dbf(name, codec='iso-8859-1')
    shp = Shp(name.replace('.dbf','.shp'))
    shape_id = 0
    for s in shp.shapes():
        seq = 0
        shape_id += 1
        for p in s.points:
            seq += 1
            o = {
                "shape_id": shape_id,
                "shape_pt_lat": p[0],
                "shape_pt_lon": p[1],
                "shape_pt_sequence": seq,
                "shape_dist_traveled": 0
            }
            print(o)

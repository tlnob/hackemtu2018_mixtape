#!/usr/bin/env python

import math
import pyproj
from glob import glob
from simpledbf import Dbf5 as Dbf
from shapefile import Reader as Shp
from geopy.distance import distance

trips = []
shapes = []

sirgas = pyproj.Proj(init="epsg:31983")
def convert(p):
    a,b = sirgas(p[0], p[1], inverse=True)
    return (b,a)
# print(sirgas(-46.703022, -23.602714))
# print(convert(sirgas(-46.703022, -23.602714)))
def rescale(bb):
    a,b = convert((bb[0], bb[1]))
    c,d = convert((bb[2], bb[3]))
    return (a,b,c,d)

for name in glob('*.dbf'):
    dbf = Dbf(name, codec='iso-8859-1')
    shp = Shp(name.replace('.dbf','.shp'))
    shape_id = 0
    for sr in shp.shapeRecords():
        s = sr.shape
        r = sr.record
        b = rescale(s.bbox)
        b = s.bbox
        seq = 0
        shape_id += 1
        last = (0,0)
        lastseq = 0
        for point in s.points:
            seq += 1
            d = 0
            p = convert(point)
            if seq > 1:
                d = distance(last, (p[0],p[1]))
            o = {
                "shape_id": shape_id,
                "shape_type": s.shapeType,
                "shape_pt_lat": p[0],
                "shape_pt_lon": p[1],
                "shape_pt_sequence": seq,
                "shape_dist_traveled": d
            }
            print(o)
            last = (p[0],p[1])
            lastseq = seq

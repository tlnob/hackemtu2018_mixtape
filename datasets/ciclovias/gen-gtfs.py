#!/usr/bin/env python

import math
from glob import glob
from simpledbf import Dbf5 as Dbf
from shapefile import Reader as Shp

trips = []
shapes = []

def dist(x, y):
    lat1, lon1 = x[0], x[1]
    lat2, lon2 = y[0], y[1]
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dp = math.radians(lat2-lat1)
    dl = math.radians(lon2-lon1)
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return 6371000 * c

for name in glob('*.dbf'):
    dbf = Dbf(name, codec='iso-8859-1')
    shp = Shp(name.replace('.dbf','.shp'))
    shape_id = 0
    mins = [
    for s in shp.shapes():
        print(s.bbox)
        seq = 0
        shape_id += 1
        last = (0,0)
        lastseq = 0
        for point in s.points:
            seq += 1
            d = 0
            p = [coord for coord in point]
            if seq > 1:
                d = dist(last, (p[0],p[1]))
            o = {
                "shape_id": shape_id,
                "shape_type": s.shapeType,
                "shape_pt_lat": p[0],
                "shape_pt_lon": p[1],
                "shape_pt_sequence": seq,
                "shape_dist_traveled": d
            }
            # print(o)
            last = (p[0],p[1])
            lastseq = seq

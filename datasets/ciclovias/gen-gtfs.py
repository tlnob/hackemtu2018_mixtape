#!/usr/bin/env python
## converte dados do CET em GTFS shapes

import math
import pyproj
from sys import stdout
from glob import glob
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

stdout.write("Creating shapes.txt")
with open("shapes.txt","w") as out:
    out.write("shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled\n")
    for name in glob('*.shp'):
        shp = Shp(name)
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
            d = 0
            for point in s.points:
                seq += 1
                p = convert(point)
                if seq > 1:
                    d += distance(last, (p[0],p[1])).meters
                out.write(str(shape_id))
                out.write(",")
                out.write("%.6f" % p[0])
                out.write(",")
                out.write("%.6f" % p[1])
                out.write(",")
                out.write(str(seq))
                out.write(",")
                out.write("%.1f" % d)
                out.write("\n")
                last = (p[0],p[1])
                lastseq = seq

            if shape_id % 10 == 0:
                stdout.write(".")
                stdout.flush()

stdout.write("OK")

from meshi import *

init()

w = 150
l = 100

box = product.box.SimpleBox(w, 40, l, panel_thick=1, pins={'height': 10})

Box(45.5, 10, 26.5, at={'x': w/2-28, 'y': -l/2}).substractFrom(box.front.panel)
Box(11.5, 10, 29, at={'x': w/2-60, 'y': -l/2}).substractFrom(box.front.panel)

cs = -w/2+68
Cylinder(8, 10, at={'x': cs, 'y': -l/2}, rot={'x': 90}).substractFrom(box.front.panel)
Box(25, 10, 15, at={'x': cs-26.75, 'y': -l/2}).substractFrom(box.front.panel)
Cylinder(3.5, 10, at={'x': cs-43.5, 'y': -l/2}, rot={'x': 90}).substractFrom(box.front.panel)
Cylinder(3.7, 10, at=(cs-43.5, -l/2, -6.8), rot={'x': 90}).substractFrom(box.front.panel)

Cylinder(12, 10, at={'x': cs-55.5, 'y': -l/2}, rot={'x': 90}).substractFrom(box.front.panel)
Box(25, 10, 12, at={'x': -w/2, 'y': -l/2}).substractFrom(box.front.panel)

box.export("~/Downloads/")

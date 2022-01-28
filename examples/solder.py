from meshi import *

init()

w = 200
l = 70

box = product.box.SimpleBox(w, 30, l, pins={'height':10})

Box(45, 10, 25, at={'x': w/2-40, 'y': -l/2}).substractFrom(box.front.panel)
Box(5, 10, 28, at={'x': w/2-75, 'y': -l/2}).substractFrom(box.front.panel)

Cylinder(5, 10, at={'x': -w/2+80, 'y': -l/2}, rot={'x': 90}).substractFrom(box.front.panel)
Box(20, 10, 10, at={'x': -w/2+50, 'y': -l/2}).substractFrom(box.front.panel)
Cylinder(10, 10, at={'x': -w/2+20, 'y': -l/2}, rot={'x': 90}).substractFrom(box.front.panel)
Box(40, 10, 20, at={'x': -w/2, 'y': -l/2}).substractFrom(box.front.panel)

#box.export("~/Downloads/")
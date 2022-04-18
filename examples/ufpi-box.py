from meshi import *

init()

w = 75
l = 90

box = product.box.SimpleBox(w, 30, l, pins={'height': 30}, bottom_thick=2)

# front
dz = -3
Cube(40, 10, 6, at={'y': -l/2, 'z': dz}).substractFrom(box.front.panel)

cs = -20+3
z = 7 + dz
Cylinder(5, 10, at=[cs, -l/2, z], rot={'x': 90}).substractFrom(box.front.panel)
Cylinder(5, 10, at=[cs+10, -l/2, z], rot={'x': 90}).substractFrom(box.front.panel)
Cylinder(5, 10, at=[cs+20, -l/2, z], rot={'x': 90}).substractFrom(box.front.panel)

# back
Cube(12, 10, 13, at={'y': l/2}).substractFrom(box.back.panel)
x = 6+8
Cylinder(5, 10, at=[x, l/2, -2], rot={'x': 90}).substractFrom(box.back.panel)
Cylinder(5, 10, at=[x, l/2, 3], rot={'x': 90}).substractFrom(box.back.panel)

box.export("~/Downloads/")

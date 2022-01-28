from meshi import *

init()

w = 150
l = 100

box = product.box.SimpleBox(w, 40, l, pins={'height': 10})

# front
Box(45.5, 10, 26.5, at={'x': w/2-28, 'y': -l/2}).substractFrom(box.front.panel)
Box(11.5, 10, 29, at={'x': w/2-60, 'y': -l/2}).substractFrom(box.front.panel)

cs = -w/2+68
Cylinder(8, 10, at={'x': cs, 'y': -l/2}, rot={'x': 90}).substractFrom(box.front.panel)
Box(25, 10, 15, at={'x': cs-26.75, 'y': -l/2}).substractFrom(box.front.panel)
Cylinder(3.5, 10, at={'x': cs-43.5, 'y': -l/2}, rot={'x': 90}).substractFrom(box.front.panel)
Cylinder(3.7, 10, at=(cs-43.5, -l/2, -6.8), rot={'x': 90}).substractFrom(box.front.panel)

Cylinder(12, 10, at={'x': cs-55.5, 'y': -l/2}, rot={'x': 90}).substractFrom(box.front.panel)
Box(25, 10, 12, at={'x': -w/2, 'y': -l/2}).substractFrom(box.front.panel)

# back
hp = w/2-30
Box(11, 10, 9, at={'x': hp, 'y': l/2}).substractFrom(box.back.panel)
box.back.add(Box(2, 5.5, 5, at={'x': hp-6.5, 'y': l/2-3.75}))
box.back.add(Box(2, 5.5, 5, at={'x': hp+6.5, 'y': l/2-3.75}))
box.back.add(part.connector.Hook(15, 13.3, 7, rot={'z':180}, at=(hp, l/2-8.5, 5.5)))
box.back.add(part.connector.Hook(15, 13.3, 7, rot={'z':180, 'y':180}, at=(hp, l/2-8.5, -5.5)))

# box.export("~/Downloads/")

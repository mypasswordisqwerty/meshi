from meshi import *

init()

top = part.wall.Grid(20, 20, border=0.5, at={'z': -4.25}, name='top')

# top box
b = wall.Grid(20, 10, border=0.5, rot={'x': 90})

top.addAt(b, [{'y': 9.5}, {'y': -9.5}])
b = wall.Grid(20, 10, border=0.5, rot={'x': 90, 'z': 90})
top.addAt(b, [{'x': 9.5}, {'x': -9.5}])
fpin = part.connector.pin.FPin(2, 4, at={'x': 8, 'y': 8, 'z': 3})
fpin.clone(at={'x': -16, 'y': -16})
fpin.clone(at={'x': -16})
fpin.clone(at={'y': -16})

bottom = top.clone('bottom', at={'x': 30})
mpin = part.connector.pin.MPin(2, 4, at={'x': 38, 'y': 8, 'z': 3}, rot={'x': 180})
mpin.clone(at={'x': -16, 'y': -16})
mpin.clone(at={'x': -16})
mpin.clone(at={'y': -16})

from meshi import *

init()

top = wall.Grid(20, 20, border=0.5, at={'z': -4.25}, name='top')

# top box
b = wall.Grid(20, 10, border=0.5, rot={'x': 90})

top.addAt(b, [{'y':9.5}, {'y':-9.5}])
b = wall.Grid(20, 10, border=0.5, rot={'x': 90, 'z':90})
top.addAt(b, [{'x':9.5}, {'x':-9.5}])

bottom = top.clone('bottom', at={'x': 30})

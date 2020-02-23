from meshi import *

init()

top = wall.grid(20, 20, border=0.5, at={'z': -10}, name='top')

# top box
b = wall.grid(20, 10, border=0.5, rot={'x': 90})

top.addAt(b, [[10, 0, -5], [-10, 0, -5]], keep=True)
b.rotate(z=90)
top.addAt(b, [[0, 10, -5], [0, -10, -5]])

bottom = top.clone('bottom')

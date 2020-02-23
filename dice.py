from meshi import *

init()

d = Box(20)

# round corners
c = Sphere(20).substract(Sphere(14))
d.substract(c)

Sphere(2).substractFromAt(d, [
    # one two
    {'z': -9}, [9, -4, -4], [9, 4, 4],
    # three
    {'y': -9}, [4, -9, -4], [-4, -9, 4],
    # four
    [4, 9, -4], [-4, 9, 4], [4, 9, 4], [-4, 9, -4],
    # five
    [-9, 4, -4], [-9, -4, 4], [-9, 4, 4], [-9, -4, -4], {'x': -9},
    # six
    [4, -4, 9], [-4, 4, 9], [4, 4, 9], [-4, -4, 9],
    {'z': 9, 'x': 4}, {'z': 9, 'x': -4},
])

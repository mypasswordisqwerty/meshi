
from .base import BaseWall
from meshi.lib import *


class Grid(BaseWall):
    OBJTYPE = 'grid_wall'

    def __init__(self, width, length=None, height=1.5,  border=2, gridWidth=1, gridSpace=10, bevel=0, **kwargs):
        self.border = border
        self.gwidth = gridWidth
        self.gspace = gridSpace
        BaseWall.__init__(self, width, length, height, bevel, **kwargs)

    def update(self):
        # grid
        cnt = int(self.length/self.gspace)+1
        at = [{'x': 0}]
        for i in range(1, cnt):
            at += [{'x': self.gspace*i}, {'x': -self.gspace*i}]
        d = Cube(self.gwidth, self.length*2, self.height-0.01, rot={"z": 45})
        self.addAt(d, at)
        d = Cube(self.gwidth, self.length*2, self.height-0.05, rot={"z": -45})
        self.addAt(d, at)
        # hole
        hole = Cube(self.width-self.border*2, self.length-self.border*2, self.height+1)
        mod = self.modifier('BOOLEAN')
        mod.object = hole.obj
        mod.operation = 'INTERSECT'
        self.apply(mod)
        # box
        b = Cube(self.width, self.length, self.height)
        if self.bevel > 0:
            mod = b.modifier('BEVEL')
            mod.segments = self.bevel
            b.apply(mod)
        b.substract(hole)
        self.add(b)

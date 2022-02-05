from .base import BaseWall
from meshi.lib import *


class Solid(BaseWall):
    OBJTYPE = 'solid_wall'

    def __init__(self, width, length=None, height=1.5, bevel=0, **kwargs):
        BaseWall.__init__(self, width, length, height, bevel, **kwargs)

    def update(self):
        b = Cube(self.width, self.length, self.height)
        if self.bevel > 0:
            mod = b.obj.modifiers.new(name='mod', type="BEVEL")
            mod.segments = self.bevel
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="mod")
        self.add(b)

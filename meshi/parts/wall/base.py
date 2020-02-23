from meshi.parts.base import BasePart
from meshi.lib import *


class BaseWall(BasePart):
    OBJTYPE = 'wall'

    def __init__(self, width, length=None, height=1.5,  bevel=0, **kwargs):
        self.width = width
        self.length = length or width
        self.height = height
        self.bevel = bevel
        BasePart.__init__(self, **kwargs)

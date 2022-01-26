from meshi.lib import BasePart


class Pin(BasePart):
    OBJTYPE = "pin"

    def __init__(self, radius=3, length=10, cradius=1, clength=5, vertices=8):
        BasePart.__init__(self)
        self.radius = radius
        self.length = length
        self.cradius = cradius
        self.clength = clength
        self.vertices = vertices


class MPin(Pin):
    OBJTYPE = "mpin"

    def __init__(self, radius=3, length=10, cradius=1, clength=5, vertices=8):
        pass


class FPin(Pin):
    OBJTYPE = "fpin"

    def __init__(self, radius=3, length=10, cradius=1, clength=5, vertices=8):
        pass

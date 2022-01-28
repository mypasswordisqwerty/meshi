from meshi.lib import BasePart, Cylinder, Box


class Pin(BasePart):
    OBJTYPE = "pin"

    def __init__(self, radius=2, height=10, cradius=None, cheight=None, **kwargs):
        self.radius = radius
        self.height = height
        self.cradius = cradius or radius/2
        self.cheight = cheight or height/2
        self.vertices = kwargs.get('vertices', 8)
        BasePart.__init__(self, **kwargs)

    def update(self):
        self.add(Cylinder(self.radius, self.height, vertices=self.vertices))


class MPin(Pin):
    OBJTYPE = "mpin"

    def __init__(self, radius=3, height=10, cradius=None, cheight=None, **kwargs):
        Pin.__init__(self, radius, height, cradius, cheight, **kwargs)

    def update(self):
        super().update()
        self.add(Cylinder(self.cradius, self.cheight+2, vertices=self.vertices, at={'z': -self.height/2+1}))


class FPin(Pin):
    OBJTYPE = "fpin"

    def __init__(self, radius=3, height=10, cradius=None, cheight=None, **kwargs):
        Pin.__init__(self, radius, height, cradius, cheight, **kwargs)

    def update(self):
        super().update()
        self.substract(Cylinder(self.cradius, self.cheight+2, vertices=self.vertices, at={'z': self.height/2}))

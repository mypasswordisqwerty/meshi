from meshi.lib import BasePart, Cylinder, Cube


class Pin(BasePart):
    OBJTYPE = "pin"

    def __init__(self, diameter=3, height=10, cdiameter=None, cheight=None, bevel=False, **kwargs):
        self.diameter = diameter
        self.height = height
        self.cdiameter = cdiameter or diameter/3
        self.cheight = cheight or height/2
        self.vertices = kwargs.get('vertices', 8)
        self.bevel = bevel
        BasePart.__init__(self, **kwargs)

    def update(self):
        self.add(Cylinder(self.diameter, self.height, vertices=self.vertices))

    def add_bevel(self, pos):
        if self.bevel:
            Cube(self.diameter*3, rot={'y': 25 if pos > 0 else -25}, at={'z': pos}).substractFrom(self)


class MPin(Pin):
    OBJTYPE = "mpin"

    def __init__(self, diameter=3, height=10, cdiameter=None, cheight=None, **kwargs):
        Pin.__init__(self, diameter, height, cdiameter, cheight, **kwargs)

    def update(self):
        super().update()
        self.add(Cylinder(self.cdiameter, self.cheight+2, vertices=self.vertices, at={'z': -self.height/2+1}))
        self.add_bevel(self.height/2)


class FPin(Pin):
    OBJTYPE = "fpin"

    def __init__(self, diameter=3, height=10, cdiameter=None, cheight=None, **kwargs):
        Pin.__init__(self, diameter, height, cdiameter, cheight, **kwargs)

    def update(self):
        super().update()
        self.substract(Cylinder(self.cdiameter, self.cheight+2, vertices=self.vertices, at={'z': self.height/2}))
        self.add_bevel(-self.height/2)

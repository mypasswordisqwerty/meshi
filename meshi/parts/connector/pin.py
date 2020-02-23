

class Connector(BasePart):
    def __init__(self, radius=3, length=10, cradius=1, clength=5, vertices=8):
        BasePart.__init__(self)
        self.radius = radius
        self.length = length
        self.cradius = cradius
        self.clength = clength
        self.vertices = vertices


class MConnector(Connector):
    def __init__(self, radius=3, length=10, cradius=1, clength=5, vertices=8):
        pass


class FConnector(Connector):
    def __init__(self, radius=3, length=10, cradius=1, clength=5, vertices=8):
        pass

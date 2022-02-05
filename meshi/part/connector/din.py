from meshi.lib import BasePart, Cube, Prism


class Din(BasePart):
    OBJTYPE = 'din_connector'

    def __init__(self, height, **kwargs):
        self.height = height
        BasePart.__init__(self, **kwargs)

    def update(self):
        self.add(Cube(5, 37, self.height))
        self.addAt(Cube(10, 1, self.height), ({'y': 36/2, 'x': -5}, {'y': -36/2, 'x': -5}))
        self.add(Prism(2, self.height, 6, at={'y': 36/2-0.5, 'x': -13}, rot={'x': 90, 'z': -90}))
        self.add(Prism(2, self.height, 6, at={'y': -36/2+0.5, 'x': -13}, rot={'x': -90, 'z': 90}))
        self.addAt(Cube(4, 2, self.height), ({'y': 36/2-0.5, 'x': -7}, {'y': -36/2+0.5, 'x': -7}))

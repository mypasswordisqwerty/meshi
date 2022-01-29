from meshi.lib import BaseProduct, Box
from meshi.part import connector, wall


class DinHolder(BaseProduct):
    def __init__(self, board_width, board_length, height=3, bevel=5, **kwargs):
        self.width = board_width
        self.height = height
        self.length = board_length
        self.pos = (board_width/2, board_length/2)
        self.bevel = bevel
        self.full_width = board_width+kwargs.get('frame_width', 15)
        self.full_length = board_length+kwargs.get('frame_length', 20)
        BaseProduct.__init__(self, **kwargs)

    def update(self):
        wl = wall.Grid(self.full_width, self.full_length, self.height, bevel=self.bevel)
        pin_diameter = self.kwargs.get('pin_diameter', 6)
        pin_cdiameter = self.kwargs.get('pin_cdiameter', 2)
        pin_height = self.kwargs.get('pin_height', 5)

        line1 = Box(self.full_width, pin_diameter, self.height, at={'y': self.pos[1]})
        line2 = Box(self.full_width, pin_diameter, self.height, at={'y': -self.pos[1]})
        line3 = Box(pin_diameter, self.length, self.height, at={'x': -self.full_width/2 + pin_diameter/2})
        zpos = pin_height/2 + self.height/2
        pin1 = connector.FPin(pin_diameter, pin_height, pin_cdiameter,
                              pin_height, at=(self.pos[0], self.pos[1], zpos))
        pin2 = connector.FPin(pin_diameter, pin_height, pin_cdiameter, pin_height,
                              at=(-self.pos[0], self.pos[1], zpos))
        pin3 = connector.FPin(pin_diameter, pin_height, pin_cdiameter, pin_height,
                              at=(self.pos[0], -self.pos[1], zpos))
        pin4 = connector.FPin(pin_diameter, pin_height, pin_cdiameter, pin_height,
                              at=(-self.pos[0], -self.pos[1], zpos))
        con = connector.Din(self.height, at={'x': -self.full_width/2})
        self.add((wl, line1, line2, pin1, pin2, pin3, pin4, con))

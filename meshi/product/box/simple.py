from meshi.lib import BaseProduct, Group, Box, Sphere
from meshi.part.connector import FPin
import bpy
import os


class SimpleBox(BaseProduct):
    OBJTYPE = 'simplebox'

    def __init__(self, width, height, length, panel_thick=2, box_thick=None, **kwargs):
        self.width = width
        self.height = height
        self.length = length
        self.panel_thick = panel_thick
        self.box_thick = box_thick or panel_thick
        self.pins = None
        BaseProduct.__init__(self, **kwargs)

    def pin_config(self):
        if not self.pins:
            pos = []
            cfg = self.kwargs.get("pins", {})
            ofs = cfg.get("offset", 10)
            conf = {'radius': cfg.get('radius', 3), 'height': cfg.get('height', self.height)}
            xofs = self.width/2 - conf['radius'] - self.box_thick + 1
            yofs = self.length/2 - conf['radius'] - ofs
            zofs = conf['height']/2 - self.height/2
            pos.append((xofs, yofs, zofs))
            pos.append((-xofs, yofs, zofs))
            pos.append((xofs, -yofs, zofs))
            pos.append((-xofs, -yofs, zofs))
            self.pins = {'pos': pos, 'conf': conf}
        return self.pins

    def create_top(self):
        self.top_thick = self.kwargs.get("top_thick", self.box_thick)
        top = Box(self.width, self.length, self.top_thick, name="top",
                  at={'z': self.height/2})
        right = Box(self.top_thick, self.length, self.height, name="right",
                    at={'x': -self.width/2+self.top_thick/2})
        left = Box(self.top_thick, self.length, self.height, name="left",
                   at={'x': self.width/2-self.top_thick/2})
        pins = []
        for x in self.pin_config()['pos']:
            pins.append(FPin(**self.pin_config()['conf'], at=x, rot={'x': 180}))
        self.top.add([left, top, right] + pins)

    def create_front(self):
        self.front_thick = self.kwargs.get("front_thick", self.panel_thick)
        panel = Box(self.width-2, self.front_thick, self.height, name="panel",
                    at={'y': -self.length/2+self.front_thick/2+1})
        self.front.add(panel)
        panel.substractFrom(self.top.top, keep=True)
        panel.substractFrom(self.top.left, keep=True)
        panel.substractFrom(self.top.right, keep=True)

    def create_back(self):
        self.back_thick = self.kwargs.get("back_thick", self.panel_thick)
        panel = Box(self.width-2, self.back_thick, self.height, name="panel",
                    at={'y': self.length/2-self.back_thick/2-1})
        self.back.add(panel)
        panel.substractFrom(self.top.top, keep=True)
        panel.substractFrom(self.top.left, keep=True)
        panel.substractFrom(self.top.right, keep=True)

    def create_bottom(self):
        self.bottom_thick = self.kwargs.get("bottom_thick", self.box_thick)
        self.bottom.add(Box(self.width, self.length, self.bottom_thick, name="panel"))
        self.bottom.move(z=-self.height/2-self.bottom_thick/2)

    def update(self):
        self.top = Group(name="top")
        self.front = Group(name="front")
        self.back = Group(name="back")
        self.bottom = Group(name="bottom")
        self.add((self.top, self.bottom, self.front, self.back))
        self.create_top()
        self.create_front()
        self.create_back()
        self.create_bottom()

    def export(self, path):
        path = os.path.expanduser(path)
        self.top.select()
        bpy.ops.export_mesh.stl(filepath=os.path.join(path, "top.stl"),  use_selection=True)
        self.bottom.select()
        bpy.ops.export_mesh.stl(filepath=os.path.join(path, "bottom.stl"),  use_selection=True)
        self.front.select()
        bpy.ops.export_mesh.stl(filepath=os.path.join(path, "front.stl"),  use_selection=True)
        self.back.select()
        bpy.ops.export_mesh.stl(filepath=os.path.join(path, "back.stl"),  use_selection=True)

from meshi.lib import BaseProduct, Group, Cube, Sphere, Cone
from meshi.part.connector import FPin
import bpy
import os


class SimpleBox(BaseProduct):
    OBJTYPE = 'simplebox'

    def __init__(self, width, height, length, panel_thick=3, box_thick=None, **kwargs):
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
            conf = {'diameter': cfg.get('diameter', 6), 'cdiameter': cfg.get('cdiameter', 2),
                    'height': cfg.get('height', self.height), 'bevel': True}
            xofs = self.width/2 - conf['diameter']/2 - self.box_thick + 0.5
            yofs = self.length/2 - conf['diameter']/2 - ofs
            zofs = conf['height']/2 - self.height/2
            pos.append(((xofs, yofs, zofs), {'x': 180}))
            pos.append(((-xofs, yofs, zofs), {'x': 180, 'z': 180}))
            pos.append(((xofs, -yofs, zofs), {'x': 180}))
            pos.append(((-xofs, -yofs, zofs), {'x': 180, 'z': 180}))
            self.pins = {'pos': pos, 'conf': conf}
        return self.pins

    def create_top(self):
        self.top_thick = self.kwargs.get("top_thick", self.box_thick)
        top = Cube(self.width, self.length, self.top_thick, name="top",
                   at={'z': self.height/2})
        right = Cube(self.top_thick, self.length, self.height, name="right",
                     at={'x': -self.width/2+self.top_thick/2})
        left = Cube(self.top_thick, self.length, self.height, name="left",
                    at={'x': self.width/2-self.top_thick/2})
        pins = []
        for x in self.pin_config()['pos']:
            pins.append(FPin(**self.pin_config()['conf'], at=x[0], rot=x[1]))
        self.top.add([left, top, right] + pins)

    def create_front(self):
        self.front_thick = self.kwargs.get("front_thick", self.panel_thick)
        self.front.add(Cube(self.width-2, self.front_thick, self.height, name="panel",
                            at={'y': -self.length/2+self.front_thick/2+1}))
        hole = Cube(self.width-2+0.2, self.front_thick+0.2, self.height+0.2,
                    at={'y': -self.length/2+self.front_thick/2+1})
        hole.substractFrom(self.top.top, keep=True)
        hole.substractFrom(self.top.left, keep=True)
        hole.substractFrom(self.top.right)

    def create_back(self):
        self.back_thick = self.kwargs.get("back_thick", self.panel_thick)
        self.back.add(Cube(self.width-2, self.back_thick, self.height, name="panel",
                           at={'y': self.length/2-self.back_thick/2-1}))
        hole = Cube(self.width-2+0.2, self.back_thick+0.2, self.height+0.2,
                    at={'y': self.length/2-self.back_thick/2-1})
        hole.substractFrom(self.top.top, keep=True)
        hole.substractFrom(self.top.left, keep=True)
        hole.substractFrom(self.top.right)

    def create_bottom(self):
        self.bottom_thick = self.kwargs.get("bottom_thick", self.box_thick)
        panel = Cube(self.width, self.length, self.bottom_thick, name="panel")
        pc = self.pin_config()
        for x in pc['pos']:
            Cone(pc['conf']['diameter'], pc['conf']['cdiameter'], self.bottom_thick,
                 at={'x': x[0][0], 'y': x[0][1]}).substractFrom(panel)
        bpos = -self.length/2 + self.front_thick + 1 + self.bottom_thick/2
        b1 = Cube(self.width - 3*self.top_thick, self.bottom_thick, self.bottom_thick+2,
                  at={'y': bpos, 'z': self.bottom_thick/2})
        b2 = Cube(self.width - 3*self.top_thick, self.bottom_thick, self.bottom_thick+2,
                  at={'y': -bpos, 'z': self.bottom_thick/2})
        self.bottom.add((panel, b1, b2))
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

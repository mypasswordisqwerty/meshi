from meshi.lib import BaseProduct, Group, Box, Sphere


class SimpleBox(BaseProduct):
    OBJTYPE = 'simplebox'

    def __init__(self, width, height, length, panel_thick=2, box_thick=None, **kwargs):
        self.width = width
        self.height = height
        self.length = length
        self.panel_thick = panel_thick
        self.box_thick = box_thick or panel_thick
        BaseProduct.__init__(self, **kwargs)

    def create_top(self):
        self.top_thick = self.kwargs.get("top_thick", self.box_thick)
        top = Box(self.width, self.length, self.top_thick, name="top",
                  at={'z': self.height/2})
        right = Box(self.top_thick, self.length, self.height, name="right",
                    at={'x': -self.width/2+self.top_thick/2})
        left = Box(self.top_thick, self.length, self.height, name="left",
                   at={'x': self.width/2-self.top_thick/2})
        self.top.add((left, top, right))

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

from meshi.lib import BasePart, Box


class Hook(BasePart):
    OBJTYPE = "hook"

    def __init__(self, len_full, len_hold, width, thick=2, hook=None, **kwargs):
        self.len_full = len_full
        self.len_hold = len_hold
        self.width = width
        self.thick = thick
        self.hook = hook or self.thick * 2
        BasePart.__init__(self, **kwargs)

    def update(self):
        self.add(Box(self.width, self.len_full, self.thick))
        len2 = self.len_full - self.len_hold
        self.add(Box(self.width, len2, self.hook,
                     at={'y': self.len_full/2 - len2/2, 'z': self.thick/2 - self.hook/2}))

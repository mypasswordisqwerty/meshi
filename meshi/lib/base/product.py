from ..group import Group


class BaseProduct(Group):
    OBJTYPE = 'product'

    def __init__(self, **kwargs):
        Group.__init__(self, **kwargs)

    def _update(self):
        self.add_to_scene()
        self.update()

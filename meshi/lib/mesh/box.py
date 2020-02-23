from .base import *
import bpy


class Box(BaseMesh):
    OBJTYPE = 'box'

    def __init__(self, width=1, length=None, height=None,  **kwargs):
        self.width = width
        self.height = height or width
        self.length = length or width
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_cube_add(size=1.0)

    def update(self):
        self.scale((self.width, self.length, self.height))

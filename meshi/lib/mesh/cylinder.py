from .base import *
import bpy


class Cylinder(BaseMesh):
    OBJTYPE = 'cylinder'

    def __init__(self, radius=0.5, height=1, vertices=32, **kwargs):
        self.radius = radius
        self.height = height
        self.vertices = vertices
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_cylinder_add(vertices=self.vertices, radius=self.radius, depth=self.height)

from ..base import BaseMesh
import bpy


class Cylinder(BaseMesh):
    OBJTYPE = 'cylinder'

    def __init__(self, diameter=1, height=1, vertices=32, radius=None, **kwargs):
        self.radius = radius or diameter/2
        self.height = height
        self.vertices = vertices
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_cylinder_add(vertices=self.vertices, radius=self.radius, depth=self.height)

from ..base import BaseMesh
import bpy


class Cylinder(BaseMesh):
    OBJTYPE = 'cylinder'

    def __init__(self, radius=0.5, height=1, vertices=32, diameter=None, **kwargs):
        self.radius = diameter/2 if diameter else radius
        self.height = height
        self.vertices = vertices
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_cylinder_add(vertices=self.vertices, radius=self.radius, depth=self.height)

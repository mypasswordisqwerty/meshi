from ..base import BaseMesh
import bpy


class Cone(BaseMesh):
    OBJTYPE = 'cone'

    def __init__(self, diameter1=2.0, diameter2=0, height=1, radius1=None, radius2=None, vertices=32, **kwargs):
        self.radius1 = radius1 or diameter1/2
        self.radius2 = radius2 or diameter2/2
        self.height = height
        self.vertices = vertices
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_cone_add(vertices=self.vertices, radius1=self.radius1,
                                        radius2=self.radius2, depth=self.height)

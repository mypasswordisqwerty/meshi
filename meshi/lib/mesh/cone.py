from ..base import BaseMesh
import bpy


class Cone(BaseMesh):
    OBJTYPE = 'cone'

    def __init__(self, radius1=1.0, radius2=0.0, height=1, diameter1=None, diameter2=None, vertices=32, **kwargs):
        self.radius1 = diameter1/2 if diameter1 else radius1
        self.radius2 = diameter2/2 if diameter2 else radius2
        self.height = height
        self.vertices = vertices
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_cone_add(vertices=self.vertices, radius1=self.radius1,
                                        radius2=self.radius2, depth=self.height)

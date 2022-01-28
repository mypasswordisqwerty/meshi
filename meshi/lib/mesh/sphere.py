from ..base import BaseMesh
import bpy


class Sphere(BaseMesh):
    OBJTYPE = 'sphere'

    def __init__(self, diameter=1, segments=32, rings=16, radius=None,  **kwargs):
        self.radius = radius or diameter/2
        self.segments = segments
        self.rings = rings
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_uv_sphere_add(segments=self.segments, ring_count=self.rings, radius=self.radius)


class ISphere(Sphere):

    def __init__(self, diameter=1, subdivisions=2, radius=None, **kwargs):
        Sphere.__init__(self, diameter, subdivisions, 0, radius, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=self.segments, radius=self.radius)

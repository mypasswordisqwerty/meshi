from ..base import BaseMesh
import bpy


class Sphere(BaseMesh):
    OBJTYPE = 'sphere'

    def __init__(self, radius=0.5, segments=32, rings=16, **kwargs):
        self.radius = radius
        self.segments = segments
        self.rings = rings
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_uv_sphere_add(segments=self.segments, ring_count=self.rings, radius=self.radius)


class ISphere(Sphere):

    def __init__(self, radius=0.5, subdivisions=2, **kwargs):
        Sphere.__init__(self, radius, subdivisions, 0, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=self.segments, radius=self.radius)

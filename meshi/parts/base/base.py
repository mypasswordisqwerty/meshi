from meshi.lib.mesh.base import BaseMesh
import bpy


class BasePart(BaseMesh):
    OBJTYPE = 'part'

    def __init__(self, **kwargs):
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.object.add(type="MESH")

    def update(self):
        raise NotImplementedError()

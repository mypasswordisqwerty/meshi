from ..base import BaseMesh
import bpy


class Prism(BaseMesh):
    OBJTYPE = 'prism'

    def __init__(self, width=1, length=None, height=None,  **kwargs):
        self.width = width
        self.height = height or width
        self.length = length or width
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        bpy.ops.mesh.primitive_cube_add(size=1.0)
        obj = bpy.context.object
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        obj.data.vertices[1].select = True
        obj.data.vertices[3].select = True
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.dissolve_edges()
        bpy.ops.object.mode_set(mode='OBJECT')

    def update(self):
        self.scale((self.width, self.length, self.height))

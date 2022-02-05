from .obj import Object3D
from .group import Group
from .base import BaseMesh, BasePart, BaseProduct
from .mesh.cube import Cube
from .mesh.sphere import Sphere, ISphere
from .mesh.cylinder import Cylinder
from .mesh.cone import Cone
from .mesh.prism import Prism
import bpy


def clean():
    keep = ['CAMERA', 'LIGHT', 'Collection']
    for x in bpy.data.objects:
        if x.type not in keep:
            bpy.data.objects.remove(x)
    for x in bpy.data.meshes:
        bpy.data.meshes.remove(x)
    for x in bpy.data.collections:
        if x.name not in keep:
            bpy.data.collections.remove(x)


def init():
    clean()
    bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'

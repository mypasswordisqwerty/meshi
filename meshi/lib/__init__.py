from .mesh.box import Box
from .mesh.sphere import Sphere, ISphere
from .mesh.cylinder import Cylinder
import bpy


def clean():
    keep = ['CAMERA', 'LIGHT']
    for x in bpy.data.objects:
        if x.type not in keep:
            bpy.data.objects.remove(x)
    for x in bpy.data.meshes:
        bpy.data.meshes.remove(x)


def init():
    clean()
    bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'

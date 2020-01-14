from .mesh.box import Box
from .mesh.sphere import Sphere, ISphere
import bpy


def clean():
    keep = ['CAMERA', 'LIGHT']
    for x in bpy.data.objects:
        if x.type not in keep:
            bpy.data.objects.remove(x)


def init():
    clean()
    bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'

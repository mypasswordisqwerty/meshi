import bpy
import math


class Object3D:
    OBJTYPE = 'object'

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.name = kwargs.get('name') or self.generate_name()
        self.obj = kwargs.get('obj')
        if not self.obj:
            self.build()
        self.obj = self._get_object()
        self._update()
        self.obj.name = self.name
        if 'at' in kwargs:
            self.move(kwargs['at'])
        if 'rot' in kwargs:
            self.rotate(kwargs['rot'])

    def _get_object(self):
        return bpy.context.object

    def _is_group(self):
        return False

    def _update(self):
        self.update()

    def generate_name(self):
        oid = 1
        while (self.OBJTYPE+str(oid)) in bpy.data.objects:
            oid += 1
        return self.OBJTYPE + str(oid)

    def clone(self, name=None, **kwargs):
        self.select()
        bpy.ops.object.duplicate(linked=0, mode='TRANSLATION')
        return Object3D(name=name, obj=True, **kwargs)

    def rename(self, name):
        self.name = name
        self.obj.name = name
        return self

    def getVector(self, vec, x=None, y=None, z=None):
        if isinstance(vec, dict):
            res = [vec.get('x', 0), vec.get('y', 0), vec.get('z', 0)]
        elif vec:
            res = [x for x in vec]
        else:
            res = [0, 0, 0]
        if x is not None:
            res[0] = x
        if y is not None:
            res[1] = y
        if z is not None:
            res[2] = z
        return res

    def unselect_all(self):
        for obj in bpy.context.selected_objects:
            obj.select_set(False)
        bpy.context.view_layer.objects.active = None

    def select(self):
        self.unselect_all()
        self.obj.select_set(True)
        bpy.context.view_layer.objects.active = self.obj
        return self

    def build(self):
        raise NotImplementedError()

    def update(self):
        pass

    def move(self, xyz=(0, 0, 0), x=None, y=None, z=None):
        self.select()
        bpy.ops.transform.translate(value=self.getVector(xyz, x, y, z))
        return self

    def moveTo(self, xyz=(0, 0, 0), x=None, y=None, z=None):
        self.select()
        self.obj.location = self.getVector(xyz, x, y, z)
        return self

    def rotate(self, xyz=(0, 0, 0), x=None, y=None, z=None):
        self.select()
        vec = self.getVector(xyz, x, y, z)
        for i, a in enumerate(['X', 'Y', 'Z']):
            if vec[i]:
                bpy.ops.transform.rotate(value=math.radians(vec[i]), orient_axis=a)
        return self

    def scale(self, xyz=(0, 0, 0), x=None, y=None, z=None):
        self.select()
        bpy.ops.transform.resize(value=self.getVector(xyz, x, y, z))
        return self

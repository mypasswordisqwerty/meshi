import bpy
import math


class BaseMesh:
    OBJTYPE = 'mesh'

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', self.generateName())
        self.obj = kwargs.get('obj')
        if not self.obj:
            self.build()
        self.obj = bpy.context.object
        self.update()
        self.setColor(kwargs.get('color', self.generateColor()))
        self.obj.name = self.name
        if 'at' in kwargs:
            self.move(kwargs['at'])
        if 'rot' in kwargs:
            self.rotate(kwargs['rot'])

    def generateName(self):
        oid = 1
        while (self.OBJTYPE+str(oid)) in bpy.data.objects:
            oid += 1
        return self.OBJTYPE + str(oid)

    def generateColor(self):
        return [1.0, 0, 0]

    def setColor(self, c):
        col = [x for x in c]
        while len(col) < 4:
            col += [1.0]
        self.obj.color = col

    def clone(self, name=None, **kwargs):
        self.select()
        bpy.ops.object.duplicate(linked=0, mode='TRANSLATION')
        return BaseMesh(name=name, obj=True, **kwargs)

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

    def select(self):
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

    def delete(self):
        bpy.data.meshes.remove(self.obj.data)
        # bpy.data.objects.remove(self.obj)
        self.obj = None

    def modifier(self, mtype, name=None):
        self.select()
        return self.obj.modifiers.new(name=name or mtype+self.name, type=mtype)

    def apply(self, modifier):
        self.select()
        return bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)

    def boolAt(self, other, at, op, keep=False):
        for x in at:
            if x is not None:
                other.moveTo(x)
            self.select()
            mod = self.modifier('BOOLEAN')
            mod.object = other.obj
            mod.operation = op
            self.apply(mod)
        if not keep:
            other.delete()
        return self

    def substractAt(self, other, at, keep=False):
        return self.boolAt(other, at, 'DIFFERENCE', keep)

    def substract(self, other, keep=False):
        return self.substractAt(other, [None], keep)

    def substractFrom(self, other, keep=False):
        other.substract(self, keep)
        return self

    def substractFromAt(self, other, at, keep=False):
        other.substractAt(self, at, keep)
        return self

    def addAt(self, other, at, keep=False):
        return self.boolAt(other, at, 'UNION', keep)

    def add(self, other, keep=False):
        return self.addAt(other, [None], keep)

    def addTo(self, other, keep=False):
        other.add(self, keep)
        return self

    def addToAt(self, other, at, keep=False):
        other.addAt(self, at, keep)
        return self

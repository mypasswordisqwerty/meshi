import bpy


class BaseMesh:
    OBJTYPE = 'mesh'

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', self.generateName())
        self.obj = None
        self.build()
        self.obj = bpy.context.object
        self.setColor(kwargs.get('color', self.generateColor()))
        self.update()
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
        vec = self.getVector(xyz, x, y, z)
        if vec[0]:
            bpy.ops.transform.rotate(value=vec[0], axis='X')
        if vec[1]:
            bpy.ops.transform.rotate(value=vec[1], axis='Y')
        if vec[2]:
            bpy.ops.transform.rotate(value=vec[2], axis='Z')
        return self

    def scale(self, xyz=(0, 0, 0), x=None, y=None, z=None):
        self.select()
        bpy.ops.transform.resize(value=self.getVector(xyz, x, y, z))
        return self

    def delete(self):
        bpy.data.objects.remove(self.obj)
        self.obj = None

    def substractAt(self, other, at, keep=False):
        for x in at:
            if x is not None:
                other.moveTo(x)
            self.select()
            mod = self.obj.modifiers.new(name='bool', type="BOOLEAN")
            mod.object = other.obj
            mod.operation = 'DIFFERENCE'
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="bool")
        if not keep:
            other.delete()
        return self

    def substract(self, other, keep=False):
        return self.substractAt(other, [None], keep)

    def substractFrom(self, other, keep=False):
        other.substract(self, keep)
        return self

    def substractFromAt(self, other, at, keep=False):
        other.substractAt(self, at, keep)
        return self

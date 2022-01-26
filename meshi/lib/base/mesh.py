from ..obj import Object3D
import bpy


class BaseMesh(Object3D):
    OBJTYPE = 'mesh'

    def __init__(self, **kwargs):
        Object3D.__init__(self, **kwargs)
        self.set_color(kwargs.get('color', self.generate_color()))

    def generate_color(self):
        return [1.0, 0, 0]

    def set_color(self, c):
        col = [x for x in c]
        while len(col) < 4:
            col += [1.0]
        self.obj.color = col

    def delete(self):
        bpy.data.meshes.remove(self.obj.data)
        # bpy.data.objects.remove(self.obj)
        self.obj = None

    def modifier(self, mtype, name=None):
        self.select()
        return self.obj.modifiers.new(name=name or mtype+self.name, type=mtype)

    def apply(self, modifier):
        self.select()
        return bpy.ops.object.modifier_apply(modifier=modifier.name)

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

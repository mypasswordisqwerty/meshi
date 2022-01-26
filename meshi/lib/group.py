from .obj import Object3D
import bpy


class Group(Object3D):
    OBJTYPE = 'group'

    def __init__(self, objects=None, **kwargs):
        self._objs = set()
        Object3D.__init__(self, **kwargs)
        if objects:
            self.add(objects)

    def _get_object(self):
        return bpy.data.collections[self.name]

    def _is_group(self):
        return True

    def build(self):
        bpy.ops.collection.create(name=self.name)

    def to_array(self, objects):
        if not isinstance(objects, (list, tuple, set)):
            objects = (objects,)
        return objects

    def add_to_scene(self):
        bpy.context.scene.collection.children.link(self.obj)

    def add(self, objects):
        for x in self.to_array(objects):
            if x._is_group():
                self.obj.children.link(x.obj)
                self._objs.add(x)
                continue
            x.select()
            bpy.ops.collection.objects_remove_all()
            self.obj.objects.link(x.obj)
            self._objs.add(x)

    def remove(self, objects):
        for x in self.to_array(objects):
            if x._is_group():
                self.obj.children.unlink(x.obj)
                self._objs.remove(x)
                continue
            x.select()
            bpy.ops.collection.objects_remove_all()
            self._objs.remove(x)

    def select(self):
        self.unselect_all()
        for x in self.obj.all_objects:
            x.select_set(True)
        return self

    def __getattr__(self, name):
        for x in self._objs:
            if name in [x.name, x.name.split('.')[0]]:
                return x
        raise Exception(f"Unknow attribute {name} for {self.name}")

from ..base import BaseMesh
import bpy


class Text(BaseMesh):
    OBJTYPE = 'text'

    def __init__(self, text, fontSize=10, fontName=None, **kwargs):
        self.text = text
        self.fontSize = fontSize
        self.fontName = fontName or 'Arial'
        BaseMesh.__init__(self, **kwargs)

    def build(self):
        # TODO: create text
        pass

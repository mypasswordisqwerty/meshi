from .lib import *
from .parts import wall, connector

__version__ = "0.1.1"


def reload():
    import importlib
    import sys
    mods = [x for x in sys.modules.keys() if x.startswith('meshi')]
    mods.sort(key=len, reverse=True)
    for x in mods:
        print(f"reloading {x}")
        importlib.reload(sys.modules[x])
    print(f"meshi reloaded v{__version__}")
    init()

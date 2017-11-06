bl_info = {
    "name": "Customize UI",
    "author": "Christophe Seux",
    "version": (0, 1),
    "blender": (2, 79, 0),
    "category": "User"}


if "bpy" in locals():
    import importlib
    importlib.reload(operators)
    importlib.reload(panels)
    importlib.reload(properties)
    importlib.reload(functions)

else:
    from .operators import *
    from .panels import *
    from .properties import *
    from .functions import *

import time
from bpy.app.handlers import persistent

@persistent
def apply_UI_handler(dummy):
    hide_panels()


def register() :
    bpy.utils.register_module(__name__)
    bpy.types.INFO_HT_header.append(menu_func)
    bpy.app.handlers.load_post.append(apply_UI_handler)

    try :
        hide_panels()
    except :
        pass

def unregister() :
    show_panels()
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_HT_header.remove(menu_func)
    bpy.app.handlers.load_post.remove(apply_UI_handler)

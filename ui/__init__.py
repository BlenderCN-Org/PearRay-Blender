import bpy


from .properties_render import draw_pearray_render


from bl_ui import properties_world
properties_world.WORLD_PT_preview.COMPAT_ENGINES.add('PEARRAY_RENDER')
properties_world.WORLD_PT_context_world.COMPAT_ENGINES.add('PEARRAY_RENDER')
properties_world.WORLD_PT_world.COMPAT_ENGINES.add('PEARRAY_RENDER')
del properties_world


from bl_ui import properties_scene
properties_scene.SCENE_PT_scene.COMPAT_ENGINES.add('PEARRAY_RENDER')
properties_scene.SCENE_PT_unit.COMPAT_ENGINES.add('PEARRAY_RENDER')
properties_scene.SCENE_PT_color_management.COMPAT_ENGINES.add('PEARRAY_RENDER')
del properties_scene


from bl_ui import properties_texture
from bl_ui.properties_texture import context_tex_datablock
for member in dir(properties_texture):
    subclass = getattr(properties_texture, member)
    try:
        subclass.COMPAT_ENGINES.add('PEARRAY_RENDER')
    except:
        pass
del properties_texture


from bl_ui import properties_material
for member in dir(properties_material):
    subclass = getattr(properties_material, member)
    if subclass not in (properties_material.MATERIAL_PT_transp_game,
                        properties_material.MATERIAL_PT_game_settings,
                        properties_material.MATERIAL_PT_physics):
        try:
            subclass.COMPAT_ENGINES.add('PEARRAY_RENDER')
        except:
            pass
del properties_material


from bl_ui import properties_data_lamp
for member in dir(properties_data_lamp):
    subclass = getattr(properties_data_lamp, member)
    if subclass not in (properties_data_lamp.DATA_PT_shadow,):
        try:
            subclass.COMPAT_ENGINES.add('PEARRAY_RENDER')
        except:
            pass
del properties_data_lamp


from bl_ui import properties_particle as properties_particle
for member in dir(properties_particle):
    subclass = getattr(properties_particle, member)
    try:
        subclass.COMPAT_ENGINES.add('PEARRAY_RENDER')
    except:
        pass
del properties_particle


def register():
    bpy.types.RENDER_PT_render.append(draw_pearray_render)
    pass


def unregister():
    bpy.types.RENDER_PT_render.remove(draw_pearray_render)
    pass
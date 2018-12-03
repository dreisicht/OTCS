import bpy

class PanelClassName(bpy.types.Panel):
    bl_idname = "OTCS"
    bl_label = "OTCS"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        col = self.layout.column(align = True)
        col.prop(context.scene, "my_string_prop")
        
import bpy

class PanelClassName(bpy.types.Panel):
    bl_idname = "SortObjectsToCollections"
    bl_label = "Sort objects to collections"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Master Collection", icon='GROUP')
        layout.prop(context.scene, "maincollection", text="")
        layout.label(text="Search tags (separate by comma)", icon='ALIGN_LEFT')
        layout.prop(context.scene, "mysearchtags", text="")
        layout.operator("scene.sortobjectstocollections", text="Start Sorting")

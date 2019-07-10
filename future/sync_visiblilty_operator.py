import bpy
bpy.context.scene.frame_current = 720


def copyVisibilityFromRenderToViewport(collectionName):
    col = bpy.data.collections[collectionName]
    print(collectionName)
    for ob in col.objects:
        #    print(ob)
        #    print(ob.hide_render)
        if ob.hide_render is True:
            ob.hide_viewport = True
        #    print("setting True")
        elif ob.hide_render is False:
            ob.hide_viewport = False
        #    print("setting False")


copyVisibilityFromRenderToViewport('Frau1')
copyVisibilityFromRenderToViewport('Mann1')
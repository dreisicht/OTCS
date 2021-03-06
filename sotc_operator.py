import bpy

moved = 0
not_moved = 0

def create_colection(search_tag):
    # creating new collection, if collection with same name exists skip step
    if search_tag not in bpy.data.collections:
        col = bpy.data.collections.new(search_tag)
        bpy.context.scene.collection.children.link(col)
        return bpy.data.collections[search_tag]
    return bpy.data.collections[search_tag]


def move(search_tag, target_collection, main_collection):
    # move objects from main collection into target collection, checking object name
    for ob in bpy.data.collections[main_collection].objects:
        # print("ob: ", ob, "ob.name: ", ob.name)
        # print("search_tag: ", search_tag, "ob.name: ", ob.name)
        # print(search_tag in ob.name)
        if search_tag in ob.name:
            # print(target_collection)
            try:
                target_collection.objects.link(ob)
                global moved
                moved = moved + 1
            except RuntimeError:
                print("Object already in collection!")
                global not_moved
                not_moved = not_moved + 1


def main(main_collection, search_tag_list):
    ## call sorting for every tag
    
    for search_tag in search_tag_list:
            target_collection = create_colection(search_tag)
            move(search_tag, target_collection, main_collection)


class SortObjectsToCollections(bpy.types.Operator):
    """Sort objects into collections"""
    bl_idname = "scene.sortobjectstocollections"
    bl_label = "#SortObjectsToCollections"
    bl_option = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        search_tag_list = bpy.context.scene.mysearchtags.split(", ")
        main_collection = bpy.context.scene.maincollection
        # print("search tag list: ", search_tag_list)
        # print("maincollection: ", bpy.types.Scene.maincollection)
        main(main_collection, search_tag_list)
        report_text = 'Moved ' + str(moved) + ' objects. Did not move ' + str(not_moved) + ' objects.'
        self.report({'INFO'}, report_text)
        return {'FINISHED'}
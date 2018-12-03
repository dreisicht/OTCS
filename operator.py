import bpy


def create_colection(search_tag):
    if search_tag not in bpy.data.collections:
        col = bpy.data.collections.new(search_tag)
        bpy.context.scene.collection.children.link(col)
        return bpy.data.collections[search_tag]
    return bpy.data.collections[search_tag]


def move(search_tag, target_collection, main_collection):
    for ob in bpy.data.collections[main_collection].objects:
        # print("ob: ", ob, "ob.name: ", ob.name)
        # print("ob.name: ", ob.name, "search_tag: ", search_tag)
        # print(search_tag in ob.name)
        if search_tag in ob.name:
            # print(target_collection)
            try:
                target_collection.objects.link(ob)
            except RuntimeError:
                print("Object already in collection!")


def sort(main_collection, search_tag):
    target_collection = create_colection(search_tag)
    move(search_tag, target_collection, main_collection)


def main(main_collection, search_tag_list):
    # main function
    for tag in search_tag_list:
        sort(main_collection, tag)

# print("START TEST")
# for ob in bpy.data.collections["new_import"].objects:
    # print(ob.name)
# print("END TEST")

# search_tag_list = list()
# search_tag_list.append("decke")
# search_tag_list.append("sichtbeton")
# search_tag_list.append("trennbeh")
# print(search_tag_list)
# main('new_import', search_tag_list)

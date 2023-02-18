def start_spring(**kwargs):
    types = {}
    for key, value in kwargs.items():
        if value not in types:
            types[value] = []
        types[value].append(key)
    collections = sorted(types.values(), key=lambda x: (-len(x), x[0]))
    result = ""
    for collection in collections:
        collection.sort()
        spring_type = kwargs[collection[0]]
        result += f"{spring_type}:\n"
        for spring_object in collection:
            result += f"-{spring_object}\n"
    return result.strip()


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


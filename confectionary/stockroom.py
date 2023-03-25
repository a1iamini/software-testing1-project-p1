RAW_MATERIALS = dict()


def add_material(material, quantity):
    global RAW_MATERIALS
    RAW_MATERIALS[material] = int(quantity)
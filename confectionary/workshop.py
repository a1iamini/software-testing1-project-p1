SWEETS_SPEC = dict()


def define_sweets_spec(sweets_name, materials):
    global SWEETS_SPEC
    materials_list = materials.split(', ')
    if sweets_name in SWEETS_SPEC:
        del SWEETS_SPEC[sweets_name]
    for m in materials_list:
        material, quantity = m.split()
        try:
            SWEETS_SPEC[sweets_name][material] = int(quantity)
        except KeyError:
            SWEETS_SPEC[sweets_name] = {material: int(quantity)}

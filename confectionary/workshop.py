import re

SWEETS_SPEC = dict()


def define_sweets_spec(sweets_name, materials):
    global SWEETS_SPEC
    materials_list = materials.split(', ')
    if sweets_name in SWEETS_SPEC:
        del SWEETS_SPEC[sweets_name]
    for m in materials_list:
        material, quantity = m.split()
        if check_values(material, quantity):
            try:
                SWEETS_SPEC[sweets_name][material] = int(quantity)
            except KeyError:
                SWEETS_SPEC[sweets_name] = {material: int(quantity)}
        else:
            return False
    return True


def check_values(material, quantity):
    if not re.match('^[0-9]+$', quantity):
        return False
    elif not re.match('^[a-zA-Z]{3,}$', material):
        return False
    return True


def required_raw_materials(sweets_name, quantity):
    requirements = dict()
    if sweets_name in SWEETS_SPEC and quantity > 0:
        for k, v in SWEETS_SPEC[sweets_name].items():
            requirements[k] = v * quantity
    else:
        raise ValueError
    return requirements

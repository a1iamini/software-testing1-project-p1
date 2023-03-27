import re
from confectionary.workshop import required_raw_materials

RAW_MATERIALS = dict()


def add_material(material, quantity):
    global RAW_MATERIALS
    if check_values(material, quantity):
        try:
            RAW_MATERIALS[material] += int(quantity)
        except KeyError:
            RAW_MATERIALS[material] = int(quantity)
        return True
    else:
        return False


def check_values(material, quantity):
    if not re.match('^[0-9]+$', quantity):
        return False
    elif not re.match('^[a-zA-Z]{3,}$', material):
        return False
    return True


def check_raw_materials(sweets_name, quantity):
    requirements = required_raw_materials(sweets_name, quantity)
    is_exist = True
    for k, v in requirements.items():
        if k in requirements and k in RAW_MATERIALS:
            if requirements[k] <= RAW_MATERIALS[k]:
                is_exist = True
            else:
                is_exist = False
                break
        else:
            is_exist = False
            break
    return is_exist


def allocate_raw_materials(sweets_name, quantity):
    requirements = required_raw_materials(sweets_name, int(quantity))
    for k, v in requirements.items():
        RAW_MATERIALS[k] -= v

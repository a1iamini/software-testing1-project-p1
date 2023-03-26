import re
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


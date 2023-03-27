from confectionary.stockroom import add_material, RAW_MATERIALS
from confectionary.store import define_sweets, update_cash_desk
from confectionary.workshop import define_sweets_spec, SWEETS_SPEC


def add(command):
    try:
        action, material, quantity = command.split()
    except ValueError:
        return False
    return add_material(material, quantity)


def define(command):
    try:
        command, materials = command.split(': ')
        *action, sweets_name, price = command.split()
        if action != ["define", "sweets"]:
            return False
        req1 = define_sweets(sweets_name, price)
        req2 = define_sweets_spec(sweets_name, materials)
    except ValueError:
        return False
    return req1 and req2


def buy(command):
    *action, sweets_name, quantity = command.split()
    quantity = int(quantity)
    requirements = dict()
    for k, v in SWEETS_SPEC[sweets_name].items():
        requirements[k] = v * quantity
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
    if is_exist:
        update_cash_desk(sweets_name, quantity)

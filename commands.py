from confectionary.stockroom import add_material, check_raw_materials, allocate_raw_materials
from confectionary.store import define_sweets, update_cash_desk
from confectionary.workshop import define_sweets_spec


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
    if action != ["customer", "buy"]:
        raise ValueError
    quantity = int(quantity)
    if check_raw_materials(sweets_name, quantity):
        update_cash_desk(sweets_name, quantity)
        allocate_raw_materials(sweets_name, quantity)
        return True
    return False

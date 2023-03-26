from confectionary.stockroom import add_material
from confectionary.store import define_sweets
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


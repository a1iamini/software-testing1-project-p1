from confectionary.stockroom import add_material
from confectionary.store import define_sweets


def add(command):
    try:
        action, material, quantity = command.split()
    except ValueError:
        return False
    return add_material(material, quantity)


def define(command):
    command, materials = command.split(': ')
    *action, sweets_name, price = command.split()
    define_sweets(sweets_name, price)

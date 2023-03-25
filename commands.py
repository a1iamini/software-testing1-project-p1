from confectionary.stockroom import add_material
from inout import print_message


def add(command):
    try:
        action, material, quantity = command.split()
    except ValueError:
        return False
    return add_material(material, quantity)

from confectionary import stockroom


def add(command):
    action, material, quantity = command.split()
    stockroom.add_material(material, quantity)

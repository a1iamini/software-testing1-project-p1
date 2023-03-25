from inout import get_command
from confectionary import stockroom


def runner():
    command = get_command()
    if command.startswith("add "):
        action, material, quantity = command.split()
        stockroom.RAW_MATERIALS[material] = int(quantity)

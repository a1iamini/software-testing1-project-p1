SWEETS = dict()


def add_sweets(command):
    global SWEETS
    command, materials = command.split(': ')
    *action, sweets_name, price = command.split()
    SWEETS[sweets_name] = int(price)

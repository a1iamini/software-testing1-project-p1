import re

SWEETS = dict()
CASH_DESK = 0


def define_sweets(sweets_name, price):
    global SWEETS
    if check_values(sweets_name, price):
        SWEETS[sweets_name] = int(price)
        return True
    return False


def check_values(sweets_name, price):
    if not re.match('^[0-9]+$', price):
        return False
    elif not re.match('^[a-zA-Z]{3,}$', sweets_name):
        return False
    return True


def update_cash_desk(sweets_name, quantity):
    global CASH_DESK
    price = SWEETS[sweets_name] * int(quantity)
    CASH_DESK += price
    return f"sweets name: {sweets_name}, price: {price} "

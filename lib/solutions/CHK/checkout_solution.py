import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    
    # We need an object with prices and special offers
    # which will be working as our DB.
    db_values = {
        'A': {
            'price': 50,
            'special_offer': {
                'qty': 3,
                'offer': 130
            }
        },
        'B': {
            'price': 30,
            'special_offer': {
                'qty': 2,
                'offer': 45
            }
        },
        'C': {
            'price': 20,
        },
        'D': {
            'price': 15,
        },
    }


    # My previous assumption about input was wrong,
    # as well as the solution
    for sku in skus_list:

        item_total = 0
        item = sku[-1]
        qty = sku[0:-1]

        if not check_values(qty, item):
            return -1

        qty = int(qty)

        if 'special_offer' in db_values[item]:
            offer_qty = db_values[item]['special_offer']['qty']
            offer = db_values[item]['special_offer']['offer']

            item_total = int(qty / offer_qty) * offer + qty % offer_qty * db_values[item]['price']
        else:
            item_total = qty * db_values[item]['price']

        total += item_total
    return total



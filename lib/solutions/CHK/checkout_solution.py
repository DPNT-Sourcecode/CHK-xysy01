
import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    skus_list = skus.split()
    
    if len(re.findall('[0-9]+[A-D]', skus)) != len(skus_list):
        return -1


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


    # as there is no example of the input string,
    # I assume it would be in "3A 2B 1C 3D" format
    for sku in skus_list:

        item_total = 0
        item = sku[-1]
        qty = int(sku[0:-1])

        if 'special_offer' in db_values[item]:
            offer_qty = db_values[item]['special_offer']['qty']
            offer = db_values[item]['special_offer']['offer']

            item_total = int(qty / offer_qty) * offer + qty % offer_qty * db_values[item]['price']
        else:
            item_total = qty * db_values[item]['price']

        total += item_total
    return total

def check_values(skus_list):
    if not qty.isdigit():
        return False
    if not bool(re.match('[A-D]', item)):
        return False

    return True


print(checkout("40A 3B 1C 2D"))

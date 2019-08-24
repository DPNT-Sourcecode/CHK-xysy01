

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

    # as there is no example of the input string,
    # I assume it would be in "3A 2B 1C 3D" format
    for qty, item in tuple(skus.split()):
        item_total = 0
        qty = int(qty)
        if db_values[item]['special_offer']:
            offer_qty = db_values[item]['special_offer']['qty']
            offer = db_values[item]['special_offer']['offer']
            item_total = qty / offer_qty * offer + qty % offer_qty * db_values[item]['price']
        else:
            item_total = qty * db_values[item]['price']

        total += item_total
    return total


print(checkout("3A 2B 1C 3D"))




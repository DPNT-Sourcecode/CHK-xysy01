

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0

    # as there is no example of the input string,
    # I assume it would be in "3A 2B 1C 3D" format

    # We need an object with prices and special offers
    # which will be working as our DB.
    db_values = {
        'A': {
            'price': 50,
            'special_offer': {
                'qty': 3,
                'offer'
            }
        }
    }

    return total


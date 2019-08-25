# We need an object with prices and special offers
# which will be working as our DB.
db_values = {
    'A': {
        'price': 50,
        'special_offer': [{
            'qty': 3,
            'offer': 130
        }, 
        {
            'qty': 5,
            'offer': 200
        }]
    },
    'B': {
        'price': 30,
        'special_offer': [{
            'qty': 2,
            'offer': 45
        }]
    },
    'C': {
        'price': 20,
    },
    'D': {
        'price': 15,
    },
    'E': {
        'price': 40,
        'special_offer': [{
            'qty': 2,
            'offer': 'B'
        }]
    },
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0

    # check for valid input
    if skus != "" and not skus.isalpha():
        return -1
    if skus != skus.upper():
        return -1
    
    # My previous assumption about input was wrong,
    # as well as the solution

    # create cart object with item quantity
    cart = {}

    for i in skus:
        if i not in cart:
            cart[i] = 1
        else:
            cart[i] += 1 

    for item in cart:
        item_total = 0
        qty = cart[item]

        if item not in db_values:
            return -1

        if 'special_offer' in db_values[item]:
            item_total = apply_offer(item, qty)
        else:
            item_total = qty * db_values[item]['price']

        total += item_total

    return total


def apply_offer(item, qty):
    offer_qty = db_values[item]['special_offer']['qty']
    offer = db_values[item]['special_offer']['offer']

    for sp in db_values[item]['special_offer']:
        offer_qty = sp['qty']
        offer = sp['offer']

    item_total = int(qty / offer_qty) * offer + qty % offer_qty * db_values[item]['price']




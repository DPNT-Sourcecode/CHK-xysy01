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
            cart[i] = { 'qty': 1, 'total': 0 }
        else:
            cart[i]['qty'] += 1 

    for item in cart:
        item_total = 0
        qty = cart[item]['qty']

        if item not in db_values:
            return -1

        if 'special_offer' in db_values[item]:
            item_total = apply_offer(item, qty)
        else:
            item_total = qty * db_values[item]['price']

        cart[item]['total'] += item_total

    return total


def apply_offer(item, qty):
    # List of objects with all offers for the item
    sp_offers = db_values[item]['special_offer']
    # Sort list from greatest to lowest by quantity
    sp_offers.sort(key=lambda x: x['qty'], reverse=True)

    # item counter need as we may apply few offers depending on quantity
    items_left = qty
    total = 0

    for sp in sp_offers:
        offer_qty = sp['qty']
        offer = sp['offer']

        if items_left >= offer_qty:
            eligible_for_offer = int(items_left / offer_qty)
            items_left -= eligible_for_offer

            offer_total = eligible_for_offer * offer           
            pass
        else:
            continue
        

    item_total = int(qty / offer_qty) * offer + qty % offer_qty * db_values[item]['price']



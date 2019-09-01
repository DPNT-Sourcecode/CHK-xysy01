# We need an object with prices and special offers
# which will be working as our DB.
db_values = {
    'A': {
        'price': 50,
        'special_offer': [{
            'qty': 3,
            'offer': 130,
            'type': 'price'
        }, 
        {
            'qty': 5,
            'offer': 200,
            'type': 'price'
        }]
    },
    'B': {
        'price': 30,
        'special_offer': [{
            'qty': 2,
            'offer': 45,
            'type': 'price'
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
            'offer': 'B',
            'type': 'freebie'
        }]
    },
    'F': {
        'price': 10,
        'special_offer': [{
            'qty': 2,
            'offer': 'F',
            'type': 'freebie'
        }]
    },
    'G': {
        'price': 20,
    },
    'H': {
        'price': 10,
        'special_offer': [{
            'qty': 5,
            'offer': 45,
            'type': 'price'
        },
        {
            'qty': 10,
            'offer': 80,
            'type': 'price'
        }]
    },
    'I': {
        'price': 35,
    },
    'J': {
        'price': 60,
    },
    'K': {
        'price': 70,
        'special_offer': [{
            'qty': 2,
            'offer': 150,
            'type': 'price'
        },]
    },
    'L': {
        'price': 90,
    },
    'M': {
        'price': 15,
    },
    'N': {
        'price': 40,
        'special_offer': [{
            'qty': 3,
            'offer': 'M',
            'type': 'freebie'
        }]
    },
    'O': {
        'price': 10,
    },
    'P': {
        'price': 50,
        'special_offer': [{
            'qty': 5,
            'offer': 200,
            'type': 'price'
        },]
    },
    'Q': {
        'price': 30,
        'special_offer': [{
            'qty': 3,
            'offer': 80,
            'type': 'price'
        },]
    },
    'R': {
        'price': 50,
        'special_offer': [{
            'qty': 3,
            'offer': 'Q',
            'type': 'freebie'
        }]
    },
    'S': {
        'price': 20,
        'special_offer': [{
            'qty': 3,
            'offer': 'STXYZ',
            'type': 'group',
            'price': 45
        }]
    },
    'T': {
        'price': 20,
        'special_offer': [{
            'qty': 3,
            'offer': 'STXYZ',
            'type': 'group',
            'price': 45
        }]
    },
    'U': {
        'price': 40,
        'special_offer': [{
            'qty': 3,
            'offer': 'U',
            'type': 'freebie'
        }]
    },
    'V': {
        'price': 50,
        'special_offer': [{
            'qty': 2,
            'offer': 90,
            'type': 'price'
        },
        {
            'qty': 3,
            'offer': 130,
            'type': 'price'
        }]
    },
    'W': {
        'price': 20,
    },
    'X': {
        'price': 17,
        'special_offer': [{
            'qty': 3,
            'offer': 'STXYZ',
            'type': 'group',
            'price': 45
        }]
    },
    'Y': {
        'price': 20,
        'special_offer': [{
            'qty': 3,
            'offer': 'STXYZ',
            'type': 'group',
            'price': 45
        }]
    },
    'Z': {
        'price': 21,
        'special_offer': [{
            'qty': 3,
            'offer': 'STXYZ',
            'type': 'group',
            'price': 45
        }]
    },
}

# create an object to store all group offers
group_offers = {
    'STXYZ': {
        'qty': 3,
        'price': 45
    }
}

# create cart object with item quantity
cart = {}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # doing some refactoring
    
    # check for valid input
    if skus != "" and not skus.isalpha():
        return -1
    if skus != skus.upper():
        return -1
    
    # reset cart
    cart.clear()
    # add group offers in the cart
    cart['group_offers'] = add_cart_group_offers()
    # populate cart
    if not populate_cart(skus):
        return -1
    # calculate total for each item
    total_per_item()
    # calculate total value
    return cart_total()

def add_cart_group_offers():
    groups = {}
    for i in group_offers:
        groups[i] = {'qty': 0, 'items': '', 'total': 0}
    
    return groups

def populate_cart(skus):
    # populate cart object with item quantity
    # leave total = 0 till later calculation 
    for i in skus:

        if i not in db_values:
            return False

        if i not in cart:
            cart[i] = {
                'qty': 1,
                'eligible_free': 0,
                'total': 0
            }
        else:
            cart[i]['qty'] += 1

    return True

def total_per_item():

    for item in cart:
        # skip group offers object 
        if item == 'group_offers':
            continue

        # do not calculate totals for items in group offers. Will do it later
        if check_group(item):
            continue

        qty = cart[item]['qty']

        if 'special_offer' in db_values[item]:
            # as we can have few offers we need to loop through them
            # and apply biggest one first
            # List of objects with all offers for the item
            sp_offers = db_values[item]['special_offer']
            # Sort list from greatest to lowest by quantity
            sp_offers.sort(key=lambda x: x['qty'], reverse=True)

            items_left = qty

            # loop through each special offer
            for sp in sp_offers:
                offer_qty = sp['qty']
                offer = sp['offer']

                # check if there is enough items to apply offer
                if items_left >= offer_qty:
                    # how many offers we can apply
                    offers_to_apply = int(items_left / offer_qty)
                    items_left -= offers_to_apply * offer_qty

                    # offers can be a bundle price or freebie
                    if sp['type'] == 'price':
                        # update cart total with offer price
                        cart[item]['total'] += offers_to_apply * offer
                    elif sp['type'] == 'freebie':
                        # add regular price for this item's total
                        cart[item]['total'] = offers_to_apply * offer_qty * db_values[item]['price']
                        # check if offer item in the cart and add it
                        if offer in cart:
                            cart[offer]['eligible_free'] += offers_to_apply

            # if any items left apply regular price
            if items_left > 0:
                cart[item]['total'] += items_left * db_values[item]['price']
        else:
            cart[item]['total'] += qty * db_values[item]['price']


# Check if item in the group and return group
# else return false
def check_group(item):
    for i in group_offers:
        if item in i:
            return i
    return False

def cart_total():
    total = 0
    for i in cart:
        item = cart[i]
        eligible_offer = 0
    
        # here check for freebies
        if item['eligible_free'] > 0:
            eligible_free = item['eligible_free']
            # check if there is price offers to calculate cost of freebies
            if 'special_offer' in db_values[i]:
                # there can be more than one offers
                sp_offers = db_values[i]['special_offer']
                sp_offers.sort(key=lambda x: x['qty'], reverse=True)

                items_left = eligible_free

                for sp in sp_offers:
                    offer_qty = sp['qty']
                    offer = sp['offer']
                    if sp['type'] == 'price':
                        # check if there is enough items to apply offer or how many we can apply
                        if items_left >=  offer_qty:
                            offers_to_apply = int(items_left / offer_qty)
                            items_left = offers_to_apply * offer_qty
                            eligible_offer += offers_to_apply * offer
                        else:
                            if item['qty'] % offer_qty == 0:
                                eligible_offer += offer - (item['qty'] - 1) * db_values[i]['price']
                            else:
                                eligible_offer += items_left * db_values[i]['price']
                    elif i == offer:
                        # check if there is enough items to apply offer or how many we can apply
                        if items_left >=  offer_qty:
                            
                            # applying freebies to itself
                            if  item['qty'] % eligible_free == 0:
                                eligible_offer += (eligible_free - 1) * db_values[i]['price']
                            else:
                                eligible_offer += eligible_free * db_values[i]['price']
                        else:
                            if offer_qty != item['qty']:
                                eligible_offer += eligible_free * db_values[i]['price']
            else:
                eligible_offer += eligible_free * db_values[i]['price']

        total += item['total'] - eligible_offer
    return total

print(checkout('STX'), 45)
# print(checkout('STXSTX'), 90)
# print(checkout('SSS'), 45)
# print(checkout('ZZZ'), 45)
# print(checkout('SSSZ'), 66)


# print("--- prev ---")
# print(checkout('NNNNNNMM'), 240)
# print(checkout('NNNMNMNN'), 240)
# print(checkout('PPPPQRUVPQRUVPQRUVSU'), 740)
# print(checkout('UUU'), 120)
# print(checkout('NNNM'), 120)
# print(checkout('NNNNM'), 160)
# print(checkout('UUUUUUUU'), 240)
# print(checkout('RRRRRRQQ'), 300)
# print(checkout('FFFFFF'), 40)
# print(checkout('AAAAAAAAAA'), 400)
# print(checkout('ABCDECBAABCABBAAAEEAA'), 665)
# print(checkout('EEEEBB'), 160)
# print(checkout('BEBEEE'), 160)
# print(checkout('FFABCDECBAABCABBAAAEEAAFF'), 695)






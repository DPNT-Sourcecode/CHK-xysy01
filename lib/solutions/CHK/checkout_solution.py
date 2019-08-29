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
    # populate cart
    populate_cart(skus)
    # calculate total for each item
    if not total_per_item():
        return -1
    # calculate total value
    return cart_total()

def populate_cart(skus):
    # populate cart object with item quantity
    # leave total = 0 till later calculation 
    for i in skus:
        if i not in cart:
            cart[i] = {
                'qty': 1,
                'eligible_free': 0,
                'total': 0
            }
        else:
            cart[i]['qty'] += 1

def total_per_item():
    for item in cart:
        qty = cart[item]['qty']

        if item not in db_values:
            return False

        if 'special_offer' in db_values:
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
                cart[item]['total'] += items_left + db_values[item]['price']
        else:
            cart[item]['total'] += qty + db_values[item]['price']

    return True

def cart_total():
    total = 0

    for i in cart:
        item = cart[i]

        # here check for freebies
        if item['eligible_free'] > 0:
            # if there is more freebies than qty
            if item['eligible_free'] > item['qty']:
                eligible_free = item['eligible_free']
            else:
                eligible_free = item['qty']

            # check if there is price offers to calculate cost of freebies
            if 'special_offer' in db_values[i]:
                # there can be more than one offers
                sp_offers = db_values[item]['special_offer']
                sp_offers.sort(key=lambda x: x['qty'], reverse=True)

                items_left = eligible_free

                for spin sp_offers:
                    if sp['type'] != 'price':
                        continue

                    offer_qty = sp['qty']
                    offer = sp['offer']

                    # check if there is enough items to apply offer or how many we can apply
                    if items_left >=  offer_qty:
                        offers_to_apply = int(items_left / offer_qty)
                        items_left = offers_to_apply * offer_qty





    return total




#     total = 0

#     # check for valid input
#     if skus != "" and not skus.isalpha():
#         return -1
#     if skus != skus.upper():
#         return -1
    
#     # My previous assumption about input was wrong,
#     # as well as the solution

#     # reset cart object
#     cart.clear()

#     # populate cart object with item quantity
#     for i in skus:
#         if i not in cart:
#             cart[i] = { 'qty': 1, 'total': 0 }
#         else:
#             cart[i]['qty'] += 1 

#     for item in cart:
#         item_total = 0
#         qty = cart[item]['qty']

#         if item not in db_values:
#             return -1

#         if 'special_offer' in db_values[item]:
#             item_total = apply_offer(item, qty)
#         else:
#             item_total = qty * db_values[item]['price']

#         cart[item]['total'] += item_total

#     # sum all the totals
#     for i in cart:
#         total += cart[i]['total']

#     return total


# def apply_offer(item, qty):
#     # List of objects with all offers for the item
#     sp_offers = db_values[item]['special_offer']
#     # Sort list from greatest to lowest by quantity
#     sp_offers.sort(key=lambda x: x['qty'], reverse=True)

#     # item counter need as we may apply few offers depending on quantity
#     items_left = qty
#     total = 0

#     for sp in sp_offers:
#         offer_qty = sp['qty']
#         offer = sp['offer']

#         if items_left >= offer_qty:
#             eligible_for_offer = int(items_left / offer_qty)
#             items_left -= eligible_for_offer * offer_qty

#             # check if offer is a price or free item 
#             if sp['type'] == 'price':
#                 total += eligible_for_offer * offer
#             elif sp['type'] == 'freebie':
#                 total += qty * db_values[item]['price']
#                 # check if an item in the cart and update total for the item
#                 if offer in cart:
#                     if cart[offer]['total'] >= eligible_for_offer * db_values[offer]['price']:
#                         cart[offer]['total'] -= eligible_for_offer * db_values[offer]['price']

#     # if any items left that are not eligible for offer apply regular price
#     if items_left > 0:
#         total += items_left * db_values[item]['price']
        
#     return total

# print(checkout("B"))





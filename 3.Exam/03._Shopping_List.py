def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."
    basket = {}
    total_price = 0
    bought_list = []
    for product, (price, quantity) in products.items():
        if len(basket) >= 5 or budget < price * quantity:
            continue
        if budget >= price * quantity:
            basket[product] = (price, quantity)
            budget -= price * quantity
            total_price += price * quantity
            bought_list.append(f"You bought {product} for {price * quantity:.2f} leva.")
    return "\n".join(bought_list)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
#
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))

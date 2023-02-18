def shop_from_grocery_list(budget, grocery_list, *products):
    budget_left = budget
    missing_products = set(grocery_list)
    purchased_products = set()
    for product in products:
        name, price = product
        if name in purchased_products:
            continue
        if name not in missing_products:
            continue
        if price > budget_left:
            break
        purchased_products.add(name)
        missing_products.remove(name)
        budget_left -= price
    if not missing_products:
        return f"Shopping is successful. Remaining budget: {budget_left:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(sorted(missing_products))}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

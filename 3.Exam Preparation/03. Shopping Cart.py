def shopping_cart(*args):
    meals = {"Soup": [], "Pizza": [], "Dessert": []}

    for arg in args:
        if arg == "Stop":
            break
        meal, product = arg
        if len(meals[meal]) < {"Soup": 3, "Pizza": 4, "Dessert": 2}[meal] and product not in meals[meal]:
            meals[meal].append(product)

    if not any(meals.values()):
        return "No products in the cart!"

    result = []
    for meal, products in sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{meal}:")
        for product in sorted(products):
            result.append(f" - {product}")

    return "\n".join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

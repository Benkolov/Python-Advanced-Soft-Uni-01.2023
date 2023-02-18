from collections import deque

milligrams_of_caffeine = deque([int(x) for x in input().split(', ')])
energy_drinks = deque([int(x) for x in input().split(', ')])


stamat_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    caffeine = milligrams_of_caffeine.pop()
    drink = energy_drinks.popleft()
    total = caffeine * drink

    if total + stamat_caffeine <= 300:
        stamat_caffeine += total
    else:

        energy_drinks.append(drink)
        stamat_caffeine -= 30
        if stamat_caffeine < 0:
            stamat_caffeine = 0


if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")

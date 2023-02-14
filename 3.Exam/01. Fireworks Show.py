from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]


creates_firework = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

while firework_effects and explosive_power:
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    effects = firework_effects.popleft()
    power = explosive_power.pop()
    power_effects = power + effects

    if power_effects % 3 == 0 and power_effects % 5 != 0:
        creates_firework['Palm Fireworks'] += 1
    elif power_effects % 3 != 0 and power_effects % 5 == 0:
        creates_firework['Willow Fireworks'] += 1
    elif power_effects % 3 == 0 and power_effects % 5 == 0:
        creates_firework['Crossette Fireworks'] += 1
    else:
        effects -= 1
        firework_effects.append(effects)
        explosive_power.append(power)

if creates_firework['Palm Fireworks'] >= 3\
        and creates_firework['Willow Fireworks'] >= 3\
        and creates_firework['Crossette Fireworks'] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")


if firework_effects:
    print("Firework Effects left: ", end='')
    print(*firework_effects, sep=", ")
if explosive_power:
    print("Explosive Power left: ", end='')
    print(*explosive_power, sep=", ")


for firework, count in creates_firework.items():
    print(f"{firework}: {count}")
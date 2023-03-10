from collections import deque


def is_bombs_pouch_filled(crafted):
    for num_bombs in crafted.values():
        if num_bombs < 3:
            return False

    return True


bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

bombs_table = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}

crafted_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

while bomb_effects and bomb_casings and not is_bombs_pouch_filled(crafted_bombs):
    bomb_effect = bomb_effects[0]
    bomb_casing = bomb_casings[-1]
    result = bomb_effect + bomb_casing
    if result in bombs_table:
        bomb_effects.popleft()
        bomb_casings.pop()
        bomb_type = bombs_table[result]
        crafted_bombs[bomb_type] += 1
    else:
        bomb_casings[-1] -= 5

if is_bombs_pouch_filled(crafted_bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for bomb, count in sorted(crafted_bombs.items()):
    print(f"{bomb}: {count}")

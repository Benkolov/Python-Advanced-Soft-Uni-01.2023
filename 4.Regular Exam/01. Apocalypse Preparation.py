from collections import deque

textiles = deque(map(int, input().split()))
medicaments = deque(map(int, input().split()))

created_items = {'MedKit': 0, 'Bandage': 0, 'Patch': 0}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    total = textile + medicament

    if total == 30:
        created_items['Patch'] += 1
    elif total == 40:
        created_items['Bandage'] += 1
    elif total == 100:
        created_items['MedKit'] += 1
    elif total > 100:
        created_items['MedKit'] += 1
        remaining = total - 100
        if medicaments:
            medicaments[-1] += remaining
        else:
            medicaments.appendleft(remaining)
    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")

created_items = {k: v for k, v in created_items.items() if v > 0}
created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
for name, amount in created_items:
    print(f"{name} - {amount}")

if medicaments:
    medicaments = reversed(medicaments)
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")


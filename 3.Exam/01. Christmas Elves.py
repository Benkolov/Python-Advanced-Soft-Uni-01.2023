from collections import deque

elves = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]

toys = 0
energy = 0
count = 0
while elves and boxes:

    elf = elves.popleft()
    if elf < 5:
        continue
    count += 1
    box_materials = boxes.pop()

    if elf < box_materials:
        elf *= 2
        elves.append(elf)
        boxes.append(box_materials)
        continue

    if count % 3 == 0 and count % 5 == 0:
        if elf >= box_materials:
            energy += box_materials * 2
            elf -= box_materials * 2
            elves.append(elf)

    elif count % 3 == 0:
        if elf >= 2 * box_materials:
            toys += 2
            energy += box_materials * 2
            elf -= box_materials * 2
            elf += 1
            elves.append(elf)
        else:
            elf *= 2
            elves.append(elf)
            boxes.append(box_materials)

    elif count % 5 == 0:
        energy += box_materials
        elf -= box_materials
        elves.append(elf)

    else:
        if elf >= box_materials:
            toys += 1
            energy += box_materials
            elf -= box_materials
            elf += 1
            elves.append(elf)


print(f"Toys: {toys}")
print(f"Energy: {energy}")

if elves:
    print("Elves left:", ', '.join(map(str, elves)))
if boxes:
    print("Boxes left:", ', '.join(map(str, boxes)))


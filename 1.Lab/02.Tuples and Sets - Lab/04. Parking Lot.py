car_numbers = set()

n = int(input())

for i in range(n):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        car_numbers.add(car_number)
    elif direction == 'OUT':
        car_numbers.remove(car_number)

if len(car_numbers) == 0:
    print("Parking Lot is Empty")
else:
    for car_number in car_numbers:
        print(car_number)

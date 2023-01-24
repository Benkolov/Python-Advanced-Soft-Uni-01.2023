vip_guests = set()
regular_guests = set()

n = int(input())

for i in range(n):
    reservation_code = input()

    if reservation_code[0].isdigit():
        vip_guests.add(reservation_code)
    else:
        regular_guests.add(reservation_code)

guest = input()
while guest != 'END':
    if guest in vip_guests:
        vip_guests.remove(guest)
    elif guest in regular_guests:
        regular_guests.remove(guest)

    guest = input()

print(len(vip_guests) + len(regular_guests))

for reservation_code in sorted(vip_guests):
    print(reservation_code)

for reservation_code in sorted(regular_guests):
    print(reservation_code)

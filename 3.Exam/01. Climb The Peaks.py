from collections import deque

food_portions = deque(int(x) for x in input().split(", "))
daily_stamina = deque(int(x) for x in input().split(", "))
peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70}
conquered_peaks = []

for peak, difficulty in peaks.items():
    while food_portions and daily_stamina:
        current_food = food_portions.pop()
        current_stamina = daily_stamina.popleft()
        if current_food + current_stamina >= difficulty:
            conquered_peaks.append(peak)
            break
    else:
        break

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print("\n".join(conquered_peaks))

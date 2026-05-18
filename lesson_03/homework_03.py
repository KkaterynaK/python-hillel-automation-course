# task 01 & 03
alice_in_wonderland = """"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough.\""""

print(alice_in_wonderland)

# task 02
for char in alice_in_wonderland:
    if char == "'":
        print(char)


# task 04
black_sea_area = 436402
azov_sea_area = 37800
total_sea_area = black_sea_area + azov_sea_area
print(f"Разом: {total_sea_area} кв. км.")


# task 05
total_goods = 375291
w_1_2 = 250449
w_2_3 = 222950

warehouse_3 = total_goods - w_1_2
warehouse_1 = total_goods - w_2_3
warehouse_2 = w_1_2 - warehouse_1

print(f"Склад 1: {warehouse_1}")
print(f"Склад 2: {warehouse_2}")
print(f"Склад 3: {warehouse_3}")

# task 06
monthly_payment = 1179
months_count = 18
computer_price = monthly_payment * months_count
print(f"Вартість комп'ютера: {computer_price} грн.")

# task 07
print(f"a) 8019 : 8 остача = {8019 % 8}")
print(f"b) 9907 : 9 остача = {9907 % 9}")
print(f"c) 2789 : 5 остача = {2789 % 5}")
print(f"d) 7248 : 6 остача = {7248 % 6}")
print(f"e) 7128 : 5 остача = {7128 % 5}")
print(f"f) 19224 : 9 остача = {19224 % 9}")

# task 08
total_cost = (4 * 274) + (2 * 218) + (4 * 35) + (1 * 350) + (3 * 21)
print(f"Загальна вартість замовлення: {total_cost} грн.")


# task 09
photos = 232
photos_per_page = 8
pages_needed = photos // photos_per_page
print(f"Ігорю знадобиться сторінок: {pages_needed}")


# task 10
distance = 1600
fuel_per_100km = 9
tank_capacity = 48

# 1) Всього бензину
total_fuel_needed = (distance / 100) * fuel_per_100km
print(f"1) Знадобиться бензину: {total_fuel_needed} л.")

# 2) Кількість заправок повного баку
refuels_needed = total_fuel_needed // tank_capacity
print(f"2) Щонайменше разів заїхати на заправку: {int(refuels_needed)}")


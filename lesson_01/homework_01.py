# task 01 == Виправте синтаксичні помилки

print("Hello", end = " ")

print("world!")

# task 02 == Виправте синтаксичні помилки

hello = "Hello"

world = "world"

if True:

  print(f"{hello} {world}!")

# task 03 == Вставте пропущену змінну у ф-цію print

for letter in "Hello world!":

  print(letter)

# task 04 == Зробіть так, щоб кількість бананів була

# завжди в чотири рази більша, ніж яблук

apples = 2

banana = apples * 4

print(banana)

# task 05 == виправте назви змінних

side_1 = 1

side_2 = 2

side_3 = 3

side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05

# та виведіть його для користувача

side_1 = 1

side_2 = 2

side_3 = 3

side_4 = 4

perimetery = side_1 + side_2 + side_3 + side_4

print(f"Периметр фігури дорівнює: {perimetery}")

"""

  # Задачі 07 -10:

  # Переведіть задачі з книги "Математика, 2 клас"

  # на мову пітон і виведіть відповідь, так, щоб було

  # зрозуміло дитині, що навчається в другому класі

"""

# task 07

"""

У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.

Скільки всього дерев посадили в саду?

apples_trees = 4

pears_trees = apples_trees + 5

plums_trees = pears_trees - 2

total_trees = apples_trees + pears_trees + plums_trees

print(f"У саду росте всього {total_trees} дерев.")

# task 08

"""

До обіда температура повітря була на 5 градусів вище нуля.

Після обіду температура опустилася на 10 градусів.

Надвечір потепліло на 4 градуси. Яка температура надвечір?

temp_start = 5

temp_after_noon = temp_start - 10

temp_evening = temp_after_noon + 4

print(f"Надвечір температура повітря стала {temp_evening} градуси.")

# task 09

"""

Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.

1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.

Скількі сьогодні дітей у театральному гуртку?

boys = 24

girls = boys // 2

boys_present = boys - 1

girls_present = girls - 2

total_children = boys_present + girls_present

print(f"Сьогодні у театральному гуртку {total_children} дітей.")

# task 10

"""

Перша книжка коштує 8 грн., друга - на 2 грн. дороже,

а третя - як половина вартості першої та другої разом.

Скільки будуть коштувати усі книги, якщо купити по одному примірнику?

book1 = 8

book2 = book1 + 2

book3 = (book1 + book2) / 2

total_price = book1 + book2 + book3

print(f"Загальна вартість усіх книг — {total_price} грн.")

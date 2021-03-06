# Отгодай число
#
# Компьютер выбирает случайное число от 1 до 100
# Игрок пытается отгодать это число, и компьютер говорит,
# предположения больше/меньше, чем загаданное число
# или попало в точку

import random

print("\t Добро пожаловать в игру 'Отгадай число'")
print("\n Я загодал натуральное число из диапазона от 1 до 100")
print("Постарайся отгадать его за минимальное число попыток")

# Начальные значения
the_number  = random.randint(1, 100)
guess = int(input("Ваше предположение: "))
tries = 1

# Цикл отгадывания
while guess != the_number:
    if guess>the_number:
        print("Меньше...")
    else:
        print("Больше...")
    guess = int(input("Ваше предположение: "))
    tries += 1
print("\a")
print("Вам удалось отгадать число! Это в самом деле ", the_number)
print("Вы затратили на отгадывание всего лишь ", tries, " попыток!\n")

input("Нажмите Enter, чтобы выйти.")

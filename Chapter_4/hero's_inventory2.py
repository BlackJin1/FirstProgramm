# Арсенал героя 2.0
# Демонстрирует создание кортежа
# Создадим кортеж с несколткими элементами и выведем его с помощью цикла for


# Создадим кортеж с несколькими элементами
inventory = ("Меч",
             "Кольчуга",
             "Щит",
             "Целебное снадобье")
# Выведем этот кортеж на экран
print("\nИтак в нашем арсенали: ")
# Выведеи все элементы последовательно
for item in inventory:
    print(item)

input("\nНажмите Enter, чтобы продолжить")

# Найдем длину картежа
print("Сейчас в нашем распоряжении ",len(inventory)," предметов.")
input("\nНажмите Enter, чтобы продолжить")

# Проверка на принадлежность кортежу с помощью in
if "Целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете")

# Вывод оного элемента с определенным индексом
index = int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом:", index, "в арсенале находиться",inventory[index])

# Отобразим срез
start = input("\nВвкдите начальный индекс среза: ")
finish = input("\nВвкдите конечный индекс среза: ")
print("Срез inventory[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])
input("\nНажмите Enter, чтобы продолжить")

# соедеиним два картежа
chest = ("Золото", "Драгоценные камни")
print("Вы нашли ларец. Вот что в нем есть: ")
print(chest)
print("Вы приобщили содержимое ларца к совему капиталу.")
inventory += chest
print("Теперь в вашем распоряжении: ")
print(inventory)
input("\nНажмите Enter, чтобы продолжить")





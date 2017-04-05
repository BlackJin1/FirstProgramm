# Арсенал героя 3.0
# Демонстрируем работу со списками

# создадим список с несколькими элементами и выведем его с помощью цикла for
inventory = ["Меч",
             "Кольчуга",
             "Щит",
             "Целебное зелье"]
input("\nИтак. в нашем арсенале: ")
for item in inventory:
    print(item)
input("\nНажмите Enter, чтобы продолжить.")

# Найдем длину списка
print("Сейяас в нашем распоряжении", len(inventory), "предметов.")
input("\nНажмите Enter, чтобы продолжить.")

# Проверка на принадлежность к списку с помощью in
if "Целебное зелье" in inventory:
    print("Вы еще поживете и повоюете")

# Вывод одного элемента с определенным индексом
index = int(input("\nВведите игдекс одного из предментов арсенала: "))
print("Под индексом", index, "в арсенале находится", inventory[index])

# Соединим два списка
chest = ["Золото", "Драгоценные камни"]
print("Вы нашли ларец, вот что в нем есть:")
print(chest)
print("Вы приобщили содержание ларца к своему арсеналу")
inventory += chest
print("Теперь в нашем распоряжении: ")
print(inventory)
input("\nНажмите Enter, чтобы продолжить.")

# Присвоение значения элемента по индексу
print("Вы обменяли мечь на арбалет.")
inventory[0] = "Арбалет"
print("Теперь ваш арсенал содержит следующие предменты: ")
print(inventory)
input("\nНажмите Enter, чтобы продолжить.")

# Приписваем значение элементам по срезу индексов
print("За золото и драгоценные камни вы купили магический кристал, способный предсказывать будущее")
inventory[4:6]= ["Магический кристал"]
print("Теперь в вашем распоряжении:")
print(inventory)
input("\nНажмите Enter, чтобы продолжить.")

# Удаляем элемент
print("В тяжелом бою был раздроблен ваш щит.")
del inventory[2]
del inventory[:2]
print("Вот что осталось в арсенале:")
print(inventory)
input("\nНажмите Enter, чтобы продолжить.")


# Обработчик исключений
# Демонстрирует обработку исключительных ситуаций try/except
try:
    num = float(input("Введите число: "))
except ValueError as e:
    print("Похоже, что это не число!")
    print(e)

# Обработка нескольких исключений
print()
for value in (None,"Привет"):
    try:
        print("Пытаюсь преобразовать в число", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже это не число!")

try:
    num = float(input("Введите число: "))
except ValueError as e:
    print("Похоже, что это не число!")
    print(e)
else:
    print("Вы ввели число:", num)
input("\n\nНажмите Enter, чтобы выйти.")
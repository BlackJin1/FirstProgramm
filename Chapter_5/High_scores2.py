# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choice = None
while choice != "0":
    print("""
    Рекорды 2.О
    О - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд""")
    choice = input("Baш выбор: ")
    print()
    # выход
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    # add score
    elif choice =="2":
        name = input("Введите имя игрока ")
        score = int(input("Введите рекорд "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("Извините, в меню нет такой команды")
input("\nВведите Enter, чтобы выйти")


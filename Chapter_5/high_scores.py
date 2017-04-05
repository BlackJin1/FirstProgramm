# Рекорды
# Демонстрирует списочные методы
scores = []
choice = None

# Вывод меню
while choice!= "0":
    print("""
    
    Рекорды:
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    3 - Удалить рекорд
    4 - Сортировать список
    """)
    choice = input("Ваш выбор: ")
    print()

    # Выход из программы
    if choice == "0":
        print("До свидания!")

    # Вывод рекордов
    elif choice == "1":
        print("Рекорды")
        for score in scores:
            print(score)

    # Добавление рекорда
    elif choice == "2":
        score = int(input("Введите свой рекорд: "))
        scores.append(score)

    # Удаление рекордов
    elif choice == "3":
        score = int(input("Какой из рекордов удалить? "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат", score, "не содержиться в списке рекодов.")

    # Сортировка рекордов
    elif choice == "4":
        scores.sort(reverse=True)

    # Непонятный пользовательский ввод
    else:
        print("Извини, вв меню нет пункта:", choice)

input("Нажмите Enter, чтобы выйти.")

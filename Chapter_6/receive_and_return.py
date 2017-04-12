# Принимай и возвращай
# Демонстрирует параметры и возвращаемые значения

def display(message):
    print(message)
def give_my_five():
    five = 5
    return five
def ask_yes_or_no(question):
    """Задает вопрос с ответ да или нет"""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

# Основная часть
display("Вам сообщение\n")
number = give_my_five()
print("Вот что возвращает функция give_my_five():", number)
answer = ask_yes_or_no("\nПожалуйста, введите 'y' или 'n' ")
print("Спасибо, что ввели:", answer)
input("\n\nНажмите Enter, чтобы выйти.")

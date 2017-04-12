# Крестики-нолики
# Компьютер играет в крестики-нолики с пользователем

# Глобальные переменные
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruct():
    """Выводит для игрока инструкцию на экран"""
    print("""
Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
Твой мозг и мой процессор сойдуться в схватке за доской игры "Крестики-нолики".
Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соответствуют полям 
доски - так, как показано ниже:
    0|1|2
    3|4|5
    6|7|8
Приготовься к бою, жалкий белковый человечишка. Вот-вот начнеться решающее сражение\n
""")

def ask_yes_no(question):
    """Задайте вопрос с ответом "Да" или "Нет" """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """
        Просит ввести число из диапазона
    :param question: Запрос диапазона
    :param low: Нижнее значение диапазона
    :param high: Верхнее значение диапазона
    """
    response = None
    while response not in (low, high):
        response = int(input(question))
    return response

def pieces():
    """Определяет принадлежность первого хода"""
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (y/n):")
    if go_first == "y":
        print("\nНу чтож, даю тебе фору, играй крестиками.")
        human = X
        computer = O
    else:
        print("\nТвоя удаль тебя погубит, буду начинать я.")
        computer = O
        human = X
    return human, computer

def new_board():
    """ Создает новую игровую доску """
    board = []
    for square in range(NUM_SQUARES):
        board.append(square)
    return board

def display_board(board):
    """ Отображает игровую доску на экран"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\n", board[3], "|", board[4], "|", board[5])
    print("\n", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    """ Создает список доступных ходов """
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY :
            moves.append(square)
    return moves

def winner(board):
    """Определяет победителя в игре."""
    WAYS_ТО_WIN = ((0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6))
    for row in WAYS_ТО_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    else:
        return None

def human_move(board,human):
    """ Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход, выбери одно из полей (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nСмешной человек, это поле уже занято!")
    print("Ладно...")
    return move

def computer_move(board, computer, human):
    """ Делает ход за компьютерного противника"""
    # Создаем рабочую копию списка, потому что функция будет менять некоторые значения в списке
    board = board[:]

    # Поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер:", end=" ")
    for move in legal_moves(board):
        board[move]=computer
        # Если в следующем ходу может победить компьютер, то выберем этот ход
        if winner(board)==computer:
            print(move)
            return move
        # Выполнив проверку, отменим внесенные изменения
        board[move]= EMPTY
    for move in legal_moves(board):
        board[move] = human
        # Если в следующий ход может победить человек, блокировать этот ход
        if winner(board) == human:
            print(move)
            return move
        # Выполнив проверку, отменим внесенные изменения
        board[move] = EMPTY
    # Поскольку в следующий ход ни одна сторона не может победить, выбираем лучшее из доступных полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """ Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """ Поздравляем победителя игры"""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья\n")
    if the_winner == computer:
        print("Как я и предсказал, победа в очередной раз осталась за мной")
    elif the_winner == human:
        print("О нет, этого не может быть, неужели ты как-то выиграл!")
    elif the_winner == TIE:
        print("Ничья!")

def main():
    display_instruct()
    computer,human = pieces()
    turn = X
    board = new_board()
    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner,computer,human)

# Запуск программы
main()
input("Введите Enter, чтобы выйти")




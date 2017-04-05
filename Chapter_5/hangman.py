# Виселица
#
# Классическая игра "Виселица". Компьютер случайным образом выбирает слово,
# которое игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за отведенное количество попыток, на экране появится фигурка повешенного.

# Импорт модуля
import random

# Константы
HANGMAN = (
    """
    ------
    |     |
    |
    |
    |
    |
    |
    |
    |
   --------------
    """,
    """
    ------
    |     |
    |     O   |
    |
    |
    |
    |
    |
    |
    --------------
    """,
    """
     ------
     |     |
     |     O  |   -+-
     |
     |
     |
     |
     |
     |
    --------------
    """,
    """
     ------
     |     |
     |     O  |  /-+-
     |
     |
     |
     |
     |
     |
     --------------
     """,
    """
     ------
     |     |
     |     O  |  /-+-/
     |
     |
     |
     |
     |
     |
     --------------
     """,
    """
     ------
     |     |
     |     O  |  /-+-/
     |     |
     |
     |
     |
     |
     |
     --------------
     """,
    """
     ------
     |     |
     |     O  |  /-+-/
     |     |
     |     | 
     |
     |
     |
     |
     --------------
     """,
    """
     ------
     |     |
     |     O  |  /-+-/
     |     |
     |     | 
     |    |  
     |    |
     |
     |
     --------------
     """,
    """
     ------
     |     |
     |     O  |  /-+-/
     |     |
     |     | 
     |    | |
     |    | |
     |
     |
     --------------
     """)
MAX_WRONG = len(HANGMAN)
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

# Инициализация переменных
word = random.choice(WORDS)
so_far = "-"*len(word) # по одному дефису, на каждую букву, которую нужно отгадать
wrong = 0 # Количество ошибок, которые сделал игрок
used = [] # Буквы, которые игрок уже предлагал

print("Добро пожаловать в игру 'Виселица', Удачи вам!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы уже предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами слово сейчас выглядит так:\n", so_far)

    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Вы уже предлагали букву:", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("\nДа! Буква",guess,"есть в слове!")
        new = ""
        for i in range(len(so_far)):
            if guess == word[i]:
                new += word[i]
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nК сожалению, буквы", guess,"нет в слове.")
        wrong+=1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nВас повесили!")
else:
    print("\nВы отгадали!")
print("\nБыло загадано слово",word)
input("\n\n")
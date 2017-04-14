# Моя зверушка
# Виртуальный питомец, о котором пользователь может заботиться

class Critter(object):
    """ Виртуальный питомец """
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif unhappiness < 10:
            m = "неплохо"
        elif unhappiness < 15:
            m = "не сказать, что хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и чувствую себя", self.mood, "\n")

    def eat(self, food=4):
        print("Мрр, спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Как вы назовете свою зверушку? ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print("""
        Моя зверушка
        0 - Выйти
        1 - Узнать о самочувствии зверушки
        2 - Покормить зверушку
        3 - Поиграть со зверушкой 
        """)

        choice = input("Ваш выбор: ")
        print()

        # Выход
        if choice == "0":
            print("До свидания")
        # Беседа со зверушкой
        elif choice == "1":
            crit.talk()
        # Кормление зверушки
        elif choice == "2":
            crit.eat()
        # Игра со зверушкой
        elif choice == "3":
            crit.play()
        # Непонятный польщовательский ввод
        else:
            print("изаините, в меню нет пукнта:",choice)

main()
input("\n\nНажмите Enter, чтобы выйти.")



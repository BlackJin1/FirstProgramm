# Закрытая зверюшка
# Демонстрирует закрытые переменные и методы
class Critter(object):
    """ Виртуальный питомец """
    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка!")
        self.name = name # Открытый атрибут
        self.__mood = mood # Закрытый атрибут

    def talk(self):
        print("\nМеня зовут:", self.name)
        print("Сйчас я чувствую себя", self.__mood, "\n")

    def __private_method(self):
        print("Это закрытый метод.")

    def public_methood(self):
        print("Это открытый метод")
        self.__private_method()


crit = Critter("Бобик", "прекрасно")
crit.talk()
crit.public_methood()

input("Нажмите Enter, чтобы выйти")
# Зверушка со свойствами
# Демонстрирует свойства
class Critter(object):
    """ Виртуальный питомец """
    def __init__(self, name):
        print("Появилась на свет новая зверушка!")
        self.__name = name;
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой!")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")
    def talk(self):
        print("Привет, меня зовут", self.name)

# Основная часть
crit = Critter("Бобик")
crit.talk()

print("\nМою зверушку зовут", end=" ")
print(crit.name)

print("\nПопробую изменить имя зверушки")
crit.name = "Мкрзик"

print("Мою зверушку зовут", end=" ")
print(crit.name)

print("\nПоробую изменить имя на пустую строку")
crit.name = ""

print("Мою зверушку зовут", end=" ")
print(crit.name)

input("\n\nНажмите Enter, чтобы выйти.")



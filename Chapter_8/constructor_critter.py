# Зверюшка с конструктором
# Демонстирует метод-конструктор

class Critter(object):
    def __init__(self, name):
        print("На свет появилась новая зверюшка")
        self.name = name

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: "+ self.name + "\n"
        return rep

    def talk(self):
        print("Привет, меня зовут", self.name, "\n")

# Основаная часть
crit1 = Critter("Бобик")
crit2 = Critter("Мурзик")

crit1.talk()
crit2.talk()
print(crit2)
print(crit2.name)
input("\n\nНажмите Enter, чтобы ыфйти")

# Просто зверюшка
# Демонстрирует простейший класс и объект
class Critter(object):
    """Виртувльный питомец"""

    def talk(self):
        print("Привет, я звверюшка, экземпляр класса Critter.")

# Основная часть
crit = Critter()
crit.talk()
input("\n\nНадмите Enter, чтобы выйти.")

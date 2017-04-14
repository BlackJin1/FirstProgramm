# Гибель пришельца
# Демонстрирует взаимодействие объектов

class Player(object):
    """ Игрок в экшен игре """
    def blast(self, enemy):
        print("Игрок стреляет во врага.\n")
        enemy.die()
class Alien(object):
    """ Враждебный пришелец - инопланетянин в экшен игре """
    def die(self):
        print("Тяжело дыша, пришелец произносит: Но вот и все, я умираю!")

# Основная часть программы
print("\t\tГибель пришельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nНажмите Enter, чтобы продолжить.")
# Карты 3.0
# Демонстритует наследование и переопределение методов
class Card(object):
    """ Одна игральная карта """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♠", "♣", "♥", "♦"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank+self.suit
        return rep

class Unprintable_Card(Card):
    """ Карты, номинал и масть которых не могут быть выведены на экран """
    def __str__(self):
        return "<нельзя напечатать>"

class Positionable_Card(Card):
    """ Карта, которую можно положить лицом или рубашкой вверх """
    def __init__(self, rank, suit, face_up=True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

# Основная часть программы
card1 = Card("A", "♦")
card2 = Unprintable_Card("A", "♣")
card3 = Positionable_Card("A", "♠")

print("Печать объекта Card:")
print(card1)

print("Печать объекта Unprintable_Card:")
print(card2)

print("Печать объекта Positionable_Card:")
print(card1)
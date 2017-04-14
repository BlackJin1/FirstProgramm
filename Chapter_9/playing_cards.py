# Карты
# Демонстрируем сочетание объектов

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
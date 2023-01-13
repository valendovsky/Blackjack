# Card class
from constants import *

class Card:

    # Initialize the suit and rank of the card
    def __init__(self, suit, rank):
        if suit in SUIT_LIST and rank in RANK_LIST:
            self.suit = suit
            self.rank = rank
        else:
            print("Значение карты должно быть 'Jack', 'Queen', 'King', 'Ace' или же целым числом, надо исправить!")
            exit()

    # Method for identifying the face value of the card
    def nominal(self):
        nominal = 0
        if self.rank == 'Jack' or self.rank == 'Queen' or self.rank == 'King':
            nominal = 10
        elif self.rank == 'Ace':
            nominal = 11
        else:
            nominal = int(self.rank)
        return nominal

    # Playing card text
    def __repr__(self):
        if self.rank == '10':
            return f'{self.rank[0]}{self.rank[1]}{self.suit[0]}'
        else:
            return f'{self.rank[0]}{self.suit[0]}'
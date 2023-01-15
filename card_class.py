# Card class
from constants import *

class Card:

    # Initialize the suit and rank of the card
    def __init__(self, suit, rank):
        if suit in SUIT_LIST and rank in RANK_LIST:
            self.suit = suit
            self.rank = rank
        else:
            print("Значение карты должно быть 'J', 'Q', 'K', 'A' или же целым числом, надо исправить!")
            exit()

    # Method for identifying the face value of the card
    def nominal(self):
        nominal = 0
        if self.rank == 'J' or self.rank == 'Q' or self.rank == 'K':
            nominal = 10
        elif self.rank == 'A':
            nominal = 11
        else:
            nominal = int(self.rank)
        return nominal

    # Playing card text
    def __repr__(self):
        return f'{self.rank}{self.suit[0]}'
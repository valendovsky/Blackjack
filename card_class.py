# Card class
class Card:
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Initialize the suit and rank of the card
    def __init__(self, suit, rank):
        if suit in Card.suits and rank in Card.ranks:
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
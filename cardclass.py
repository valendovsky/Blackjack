# Card class

class Card:
    suit_list = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    rank_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    # Initialize the suit and rank of the card
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if self.suit not in Card.suit_list:
            print("Значение карты должно быть 'Jack', 'Queen', 'King', 'Ace' или же целым числом, надо исправить!")
            exit()
        elif self.rank not in Card.rank_list:
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
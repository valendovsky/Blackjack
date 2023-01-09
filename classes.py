# Card class

class Card:
     # Initialize the suit and rank of the card
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Method for identifying the face value of the card
    def nominal(self):
        nominal = 0
        try:
            if self.rank == 'Jack' or self.rank == 'Queen' or self.rank == 'King':
                nominal = 10
            elif self.rank == 'Ace':
                nominal = 11
            else:
                nominal = int(self.rank)
        except ValueError:
                print("Значение карты должно быть 'Jack', 'Queen', 'King', 'Ace' или же целым числом, надо исправить!")
                exit()
        return nominal

    # Playing card text
    def __repr__(self):
        return f'{self.rank[0]}{self.suit[0]}'
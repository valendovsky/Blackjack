# Карточная игра BlackJack
from constants import *
from card_class import *
from random import shuffle


# This function reads information from a settings text file and checks the received data for errors.
def get_settings():
    with open(FILE_ADDRESS, 'r') as rd:
        lst = rd.readlines()

    dict_settings = {}
    # The next block checks the received information by data type
    try:
        dict_settings[POINT_SHUFFLE] = float(lst[0])
        dict_settings[CONNECTION] = str.rstrip(str(lst[1]))
        dict_settings[PLAYERS_NUM] = int(lst[2])
        dict_settings[MIN_BET] = int(lst[3])
        dict_settings[MAX_BET] = int(lst[4])
    except ValueError:
        print('Некорректное значение в файле настроек! 1,4,5,6 - это целые числа, 2 - число с точкой, а 3 - строчное выражение.')
        exit()

    # The next block checks the received information for logical errors.
    if dict_settings[POINT_SHUFFLE] < SHUFFLE_MIN or dict_settings[POINT_SHUFFLE] > SHUFFLE_MAX:
        print('Диапазон точки шаффла должен быть между 3,5 и 4,5 колоды, надо исправить!')
    elif dict_settings[CONNECTION] != CONSOLE and dict_settings[CONNECTION] != NETWORK:
        print('Соединение должно быть либо console либо network, надо исправить!')
    elif dict_settings[PLAYERS_NUM] < PLAYERS_MIN or dict_settings[PLAYERS_NUM] > PLAYERS_MAX:
        print('Количество игроков не может быть меньше 1 и больше 7. Надо исправить!')
    elif dict_settings[MIN_BET] > dict_settings[MAX_BET] or dict_settings[MIN_BET] <= 0:
        print('Значение минимальной ставки не может быть больше значения максимальной или ноль и меньше. Надо исправить!')
    else:
        return dict_settings
    exit()


# This function completes the deck list to form a deck of cards.
# Output parameter
def get_deck(out_deck):
    for suit in Card.suits:
        for rank in Card.ranks:
            out_deck.append(Card(suit, rank))
    out_deck *= DECK_VALUE


# This feature shuffles six blackjack decks.
# Output parameter
def shuffle_deck(out_deck):
    # Fisher-Yates Shuffle Algorithm
    shuffle(out_deck)


# This function outputs six decks shuffled in rows of 52
def print_deck(row_deck):
    for i in range(len(row_deck)):
        if not i % 52 == 0:
            print(row_deck[i], end=' ')
        else:
            print('')
    print('\n')



def main():
    settings = get_settings()

    deck = []

    get_deck(deck)

    shuffle_deck(deck)

    print_deck(deck)




if __name__ == '__main__':
    main()

# by mentorship

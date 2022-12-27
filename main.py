# Карточная игра BlackJack

list_settings = get_settings(file)

def main():
    list_settings = get_settings(file)
    list_deck = get_deck(settings, deck)
    shuffle = shuffle_deck(settings, deck, point_shuffle)
    print_deck(deck)
    play_blackjack(deck, settings.console, players)
    print_deck(deck)
    pass


if __name__ == '__main__':
    main()

# by mentorship

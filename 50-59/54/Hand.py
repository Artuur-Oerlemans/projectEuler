import functools
from Card import Card


class Hand:
    cards: list[Card]

    def __init__(self, str_hand: str):
        str_cards = str_hand.split(' ')
        self.cards = [Card(str_card) for str_card in str_cards]
        self.cards.sort(reverse=True)
        print(self)

    def __str__(self):
        strings = [str(card) for card in self.cards]
        return ' '.join(strings)


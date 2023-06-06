import functools


@functools.total_ordering
class Card:
    rank: str
    suit: str

    def __init__(self, str_card: str):
        self.rank = str_card[0]
        self.suit = str_card[1]

    def __lt__(self, other):
        return self.rank_to_int() < other.rank_to_int()

    def __eq__(self, other):
        return self.rank_to_int() == other.rank_to_int()

    def rank_to_int(self):
        match self.rank:
            case "T":
                return 10
            case "J":
                return 11
            case "Q":
                return 12
            case "K":
                return 13
            case "A":
                return 14
            case _:
                return int(self.rank)

    def __str__(self):
        return self.rank + self.suit

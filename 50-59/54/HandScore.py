import functools

from Card import Card


@functools.total_ordering
class HandScore:
    score: int
    secondary_sort: list[int]
    cards: list[Card]

    def __init__(self, score: int, secondary_sort: list[int], cards: list[Card]):
        self.score = score
        self.secondary_sort = secondary_sort
        self.cards = cards

    def __lt__(self, other):
        if self.score < other.score:
            return True
        elif self.score > other.score:
            return False

        if self.secondary_sort < other.secondary_sort:
            return True
        elif self.secondary_sort > other.secondary_sort:
            return False

        return self.cards < other.cards

    def __eq__(self, other):
        return self.score == other.score and self.secondary_sort == other.secondary_sort and self.cards == other.cards

    def __str__(self):
        match self.score:
            case 8:
                score_name = "Straight Flush"
            case 7:
                score_name = "Four of a Kind"
            case 6:
                score_name = "Full House"
            case 5:
                score_name = "Flush"
            case 4:
                score_name = "Straight"
            case 3:
                score_name = "Three of a Kind"
            case 2:
                score_name = "Two Pairs"
            case 1:
                score_name = "One Pair"
            case 0:
                score_name = "High Card"
            case _:
                score_name = "unknown"
        return str(self.score) + " " + score_name + " " + str(self.secondary_sort)
